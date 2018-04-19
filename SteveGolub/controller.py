#!/usr/bin/env python3
import logging

import logger
import model
import view


def holdings_loop():

    quit_input = ['q', 'Quit', 'quit']      # exit the game

    while True:
        user_input = view.menu().lower()

        if user_input.isdigit():
            # assume numeric input is CIK
            display_holdings(user_input)
        else:
            if user_input in quit_input or len(user_input) == 0:
                view.show_user_results('Thanks for playing.  Goodbye!')
                switched_on = False
                return False
            else:
                # company name lookup
                cik = model.get_cik_from_name(user_input)
                if len(cik) > 0:
                    display_holdings(cik)
                else:
                    view.show_user_results('CIK not found for {0}'.
                                           format(user_input))

    return True


def display_holdings(cik):
    """
    :param cik: Desired CIK
    :return:
    """
    docs_link = model.get_fund_doc_link_by_cik(cik)
    holdings_link = model.get_fund_holdings_xml_link(docs_link)
    holdings = model.get_fund_holdings(holdings_link)
    for h in holdings:
        s = '\t'.join(h)
        print('{0}'.format(s))


def tester(module_logger):

    # https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001166559&owner=include&count=40&hidefilings=0
    # https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001478215&owner=include&count=40&hidefilings=0
    cik_list = ['0001166559', '0001478215']

    for cik in cik_list:
        docs_link = model.get_fund_doc_link_by_cik(cik)
        print('docs_link:', docs_link)

        holdings_link = model.get_fund_holdings_xml_link(docs_link)
        print('holdings_link:', holdings_link)

        holdings = model.get_fund_holdings(holdings_link)
        for h in holdings:
            s = '\t'.join(h)
            module_logger.info('{0}'.format(s))

    return True


def main():
    # Start logger
    app_name = __file__.split('.')[0]
    logger.start_logger(app_name)

    module_logger = logging.getLogger('{app_name}.controller'.format(app_name=app_name))
    module_logger.info('===== Starting =====')

    # start the game
    holdings_loop()


if __name__ == '__main__':
    main()
