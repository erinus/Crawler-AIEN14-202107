import json

import requests

def GetProduct(pid):
    response = requests.get(
        url=f'https://ecapi.pchome.com.tw/ecshop/prodapi/v2/prod/{pid}-000&fields=Name,Price,Discount,Pic,Weight,ISBN,Qty,Bonus,isBig,isSpec,isCombine,isDiy,isRecyclable,isCarrier,isMedical,isBigCart,isSnapUp,isDescAndIntroSync,isFoodContents,isHuge,isEnergySubsidy,isPrimeOnly,isPreOrder24h,isWarranty,isLegalStore,isFresh,isBidding,isSet,Volume,isArrival24h,isETicket,ShipType,isO2O,RealWH,ShipDay,ShipTag&_callback=jsonp_prod',
        headers={
            'referer': f'https://24h.pchome.com.tw/prod/{pid}',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
    )

    if response.status_code != 200:
        print('not 200')
        return

    with open('pchome24.js', 'wb') as f:
        f.write(response.content)

    text = response.text[15:-48]
    d = json.loads(text)
    print(d[f'{pid}-000']['Name'])
    print(d[f'{pid}-000']['Price']['P'])


if __name__ == '__main__':
    pid = 'DPADS4-A9009M974'
    GetProduct(pid)