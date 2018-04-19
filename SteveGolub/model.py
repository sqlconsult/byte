from bs4 import BeautifulSoup
import os
import requests
from xml.etree import ElementTree


def download_file(link, file_nm):
    """

    :param link:     Link to download file
    :param file_nm:  Target output file name
    :return:
    """
    try:
        success = False
        num_try = 1         # max of 10 attempts
        max_try = 10
        while not success and num_try <= max_try:
            # download file
            cmd = 'curl "{0}" > {1}'.format(link, file_nm)
            # print('curl cmd:', cmd)
            os.system(cmd)
            # is it there?
            if os.path.isfile(file_nm):
                with open(file_nm, 'r') as f:
                    line = f.readline()
                    if line[1] == '<!DOCTYPE':
                        num_try += 1
                    else:
                        success = True
        return True
    except:
        return False
    pass


def get_cik_lookup_data():
    """
    :return: True if file successfully downloaded, else False
    """
    #
    # Get company name to CIK look-up file
    #
    link = "https://www.sec.gov/Archives/edgar/cik-lookup-data.txt"
    path, file_nm = os.path.split(link)
    download_file(link, file_nm)


def get_fund_doc_link_by_cik(cik):
    """
    :param cik: Central Index Key (CIK) to lookup
    :return:    Dictionary containing fund information (holdings)
    """
    #
    # Step 1: Get documents filed by the fund
    #    https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001478215&owner=include&count=40&hidefilings=0
    #
    documents_url = "https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&" \
                    "CIK={0}&owner=include&count=40&hidefilings=0".format(cik)
    # print(documents_url)
    response = requests.get(documents_url).text
    soup = BeautifulSoup(response, 'html.parser')

    # with open('test_doc/soup_{0}.txt'.format(cik), 'w+') as out:
    #     out.write(str(soup))

    # get the tables (the class names may be different between CIKs)
    tbl_class = ''
    tables = soup.findAll("table")

    # with open('test_doc/table_{0}.txt'.format(cik), 'w+') as out:
    #     out.write(str(tables))

    for table in tables:
        if table.has_attr('class'):
            tbl_class = table['class']

    if tbl_class == '':
        return ''

    # this table contains the documents
    # table = soup.find("table", {"class_": "TheTitle"})
    table = soup.find("table", class_=tbl_class)
    # print(80*'=')
    # print(tbl_class)
    # print(table)
    # print(80*'=')

    # now that we found the table with the documents, loop
    # over all table rows until we find the first 13F-HR document
    rows = table.findAll('tr')
    # print(len(rows))
    # print(80*'=')
    found = False
    for row in rows:
        tds = row.findAll('td')
        for td in tds:
            # print(td)
            # print(80 * '=')
            contents = td.renderContents()
            text = contents.strip().decode("utf-8")
            # print('text:', text.strip())
            # print(80 * '=')

            # find cell with 13F-HR text
            if text == '13F-HR':
                found = True
                continue

            elif found:
                # next cell contains documents link
                # print('get link from:', td)
                # https://www.sec.gov/Archives/edgar/data/1166559/000110465918009713/0001104659-18-009713-index.htm

                a = td.find('a')
                if a is not None:
                    link = 'https://www.sec.gov{0}'.format(a['href'])
                    # link = a['href']
                    # print(link)
                    return link

    # link not found return empty string
    return ''


def get_fund_holdings(link):
    """
    :param link: Link to fund holdings XML file
    :return:     Dictionary with fund holdings
    """
    #
    # download fund holdings xml file
    #
    path, file_nm = os.path.split(link)
    ret_sts = download_file(link, file_nm)

    # return an empty list when unable to download xml file
    if not ret_sts:
        return []

    # file_nm = 'a18-5576_1informationtable.xml'

    tree = ElementTree.parse(file_nm)
    root = tree.getroot()

    # column names
    header = ['nameOfIssuer',
              'titleOfClass',
              'cusip',
              'value',
              'sshPrnamt',
              'sshPrnamtType',
              'investmentDiscretion',
              'Sole',
              'Shared',
              'None']

    # these elements have additional info
    sub_details = ['shrsOrPrnAmt', 'votingAuthority']

    # initialize return value
    result = [header]

    # loop over all nodes in toot
    for info_table in root:
        # 1 row for each node
        row = [''] * len(header)

        # loop over all nodes
        for detail in info_table:
            # get tag name
            pos = len(detail.tag) - detail.tag.rfind('}') - 1
            tag_nm = detail.tag[-pos:]

            # if the tag has additional details, get them
            if tag_nm in sub_details:
                for sd in detail:
                    s_pos = len(sd.tag) - sd.tag.rfind('}') - 1
                    s_tag_nm = sd.tag[-s_pos:]
                    s_i = header.index(s_tag_nm)
                    row[s_i] = sd.text

            else:
                # put value into row
                i = header.index(tag_nm)
                row[i] = detail.text

        # add row to result
        result.append(row)

    return result


def get_cik_from_name(name):
    """
    :param name: Company name to look up
    :return:     Dictionary containing fund information (holdings)
    """
    ret_val = ''
    if get_cik_lookup_data():
        with open('cik-lookup-data.txt', 'r') as f:
            for line in f:
                line_parts = line.split(':')
                if line_parts[0] == name:
                    cik = line_parts[1]
                    return cik
    return ret_val


def get_fund_holdings_xml_link(link):
    """
    :param link: Given a fund documents link retrieve the fund holdings XML link
    :return:
    """
    response = requests.get(link).text
    soup = BeautifulSoup(response, 'html.parser')

    # get the tables (the class names may be different between CIKs)
    tbl_class = ''
    tables = soup.findAll("table")

    for table in tables:
        if table.has_attr('class'):
            tbl_class = table['class']

    if tbl_class == '':
        return ''

    table = soup.find("table", class_=tbl_class)

    rows = table.findAll('tr')
    found = False
    for row in rows:
        tds = row.findAll('td')
        for td in tds:
            # print(td)
            # print(80 * '=')
            contents = td.renderContents()
            text = contents.strip().decode("utf-8")

            if text == 'INFORMATION TABLE':
                found = True
                continue

            elif found:
                # next cell contains documents link
                # print('get link from:', td)
                # https://www.sec.gov/Archives/edgar/data/1166559/000110465918009713/a18-5694_1informationtable.xml

                a = td.find('a')
                if a is not None:
                    a_text = td.string
                    link = 'https://www.sec.gov{0}'.format(a['href'])
                    # print('link:', link)
                    # print('text:', a_text)
                    if link[-3:] == 'xml' and a_text[-3:] == 'xml':
                        # link = a['href']
                        # print(link)
                        return link

    return ''
