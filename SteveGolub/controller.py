import model
import view


def holdings_loop():

    quit_input = ['q', 'Quit']      # exit the game

    switched_on = True
    while switched_on:
        user_input = view.menu().lower()

        if user_input.isdigit():
            # cik lookup
            ret_val = model.get_fund_holdings_by_cik(user_input)
            pass
        else:
            if user_input in quit_input:
                view.show_user_results('Thanks for playing.  Goodbye!')
                switched_on = False
                break
            else:
                # company name lookup
                ret_val = model.get_fund_holdings_by_name(user_input)
                pass

    return True


def tester():
    # https://www.sec.gov/cgi-binm/browse-edgar?action=getcompany&CIK=0001478215&owner=include&count=40&hidefilings=0
    cik = '0001478215'
    docs_link = model.get_fund_doc_link_by_cik(cik)
    print('docs_link:', docs_link)

    holdings_link = model.get_fund_holdings_xml_link(docs_link)
    print('holdings_link:', holdings_link)

    model.get_fund_holdings(holdings_link)

    return True


if __name__ == '__main__':
    # start the trading
    # holdings_loop()
    tester()

