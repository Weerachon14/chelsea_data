import requests
# from bs4 import BeautifulSoup
import logging
import os
import json
logging.basicConfig(level=logging.INFO)

def scarping_chelsea():
    cookies = {
        '_ga': 'GA1.1.423192290.1734147882',
        'FPID': 'FPID2.2.aaiRlnu4qt1n%2FSB%2FsXsLP7gHrX0po70tECSpTvTHVDw%3D.1734147882',
        'Chelsea.IsLoggedIn': 'true',
        'Chelsea.ProfileImageUrl': 'https%3A%2F%2Flh3.googleusercontent.com%2Fa%2FACg8ocIQHO7_kQBt1Z8EOWCEDQXHU02XuarYG2pH_LGgN4VOHBJ04-K3%3Ds96-c',
        'OptanonAlertBoxClosed': '2025-02-04T12:29:10.625Z',
        'eupubconsent-v2': 'CQMSZygQMSZygAcABBENBbFsAP_gAEPgAChQKytX_G__bWlr8X73aftkeY1P99h77sQxBhbJE-4FzLvW_JwXx2E5NAz6tqIKmRIAu3TBIQNlHJDURVCgaogVrSDMaEyUoTNKJ6BkiFMRI2dYCFxvm4tjeQCY5vr991dx2B-t7dr83dzyy4hHn3a5_2S0WJCdA4-tDfv9bROb-9IOd_x8v4v4_F7pE2_eT1l_tWvp7D9-cts_9XW99_fbff9Pn_-uB_-_X_vf_H37oKyAEmGhUQBlkSEhBoGEECAFQVhARQIAgAASBogIATBgU7AwAXWEiAEAKAAYIAQAAgyABAAAJAAhEAEABQIAAIBAoAAwAIBgIAGBgADABYCAQAAgOgYpgQQCBYAJGZFQpgQgAJBAS2VCCQBAgrhCEWeARAIiYKAAAEAApAAEBYLA4kkBKxIIAuIJoAACABAIIAChFJ2YAggDNlqrwZNoytMCwfMFz2mAZAEQRk5JsQAA.f_wACHwAAAAA',
        '__spdt': '3b5d9272cbf74d35b5d8480d48487110',
        '_tt_enable_cookie': '1',
        '_ttp': 'XfWVeUWImhrbYUV3PXf3iTpsjtu.tt.1',
        '_scid': 'FN13FfQRhjnl79qdjQ6f0QfiM5HRPmVb',
        '_clck': 'wcusc2%7C2%7Cftr%7C0%7C1861',
        '_sctr': '1%7C1740502800000',
        'OptanonConsent': 'isGpcEnabled=0&datestamp=Wed+Feb+26+2025+15%3A56%3A50+GMT%2B0700+(Indochina+Time)&version=202408.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=b10db874-e5dc-4d8e-a006-c30784fabda5&interactionCount=2&isAnonUser=1&landingPath=NotLandingPage&groups=C0003%3A1%2CC0004%3A1%2CC0002%3A1%2CC0005%3A1%2CC0001%3A1%2CV2STACK42%3A1&AwaitingReconsent=false&intType=1&geolocation=TH%3B10',
        '_scid_r': 'Il13FfQRhjnl79qdjQ6f0QfiM5HRPmVbSPasFQ',
        '_ga_0SXVVHPVKT': 'GS1.1.1740565117.10.1.1740567899.0.0.0',
        '.AspNetCore.Cookies': '',
        '.AspNetCore.CookiesC1': '',
        '.AspNetCore.CookiesC2': '',
        '__gads': 'ID=086a1f2ff3b93b7f:T=1734147882:RT=1751793781:S=ALNI_MbFlc2epxawJb6dJV547TzESz7-nA',
        '__gpi': 'UID=00000f8f0542ee95:T=1734147882:RT=1751793781:S=ALNI_MbAiIsaXVTFp768VcMdCz_PiGuX6A',
        '__eoi': 'ID=733e6ae3a82970fc:T=1750819223:RT=1751793781:S=AA-AfjZbwA4hCTwYXsgJyxFQmalz',
        '_ga_TIKTOK': 'GS2.1.s1751793780$o12$g0$t1751793780$j60$l0$h1856245207',
        '_ga_FBMAIN': 'GS2.1.s1751793780$o12$g0$t1751793780$j60$l0$h1202007613',
        'FPLC': 'Ggp5NRLF79rrZNHeu6dirieeJAfkQaGps7buGisVClqDpAzoogrYZkWQ9kefELgBUxz1Obo9hZ%2FqGIabiOEz6ic%2BkHIZH4Lf03PccknwDBNaVd5r8D0ta%2BVNxtcVTQ%3D%3D',
        '__cmpcccu75435': 'aCQUJoT7AAqWAGQwiLUKYAA',
    }

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'priority': 'u=1, i',
        'referer': 'https://www.chelseafc.com/en/teams/profile/reece-james',
        'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
        'cache-control': 'no-cache',
        'pragma': 'no-cache',
        # 'cookie': '_ga=GA1.1.423192290.1734147882; FPID=FPID2.2.aaiRlnu4qt1n%2FSB%2FsXsLP7gHrX0po70tECSpTvTHVDw%3D.1734147882; Chelsea.IsLoggedIn=true; Chelsea.ProfileImageUrl=https%3A%2F%2Flh3.googleusercontent.com%2Fa%2FACg8ocIQHO7_kQBt1Z8EOWCEDQXHU02XuarYG2pH_LGgN4VOHBJ04-K3%3Ds96-c; OptanonAlertBoxClosed=2025-02-04T12:29:10.625Z; eupubconsent-v2=CQMSZygQMSZygAcABBENBbFsAP_gAEPgAChQKytX_G__bWlr8X73aftkeY1P99h77sQxBhbJE-4FzLvW_JwXx2E5NAz6tqIKmRIAu3TBIQNlHJDURVCgaogVrSDMaEyUoTNKJ6BkiFMRI2dYCFxvm4tjeQCY5vr991dx2B-t7dr83dzyy4hHn3a5_2S0WJCdA4-tDfv9bROb-9IOd_x8v4v4_F7pE2_eT1l_tWvp7D9-cts_9XW99_fbff9Pn_-uB_-_X_vf_H37oKyAEmGhUQBlkSEhBoGEECAFQVhARQIAgAASBogIATBgU7AwAXWEiAEAKAAYIAQAAgyABAAAJAAhEAEABQIAAIBAoAAwAIBgIAGBgADABYCAQAAgOgYpgQQCBYAJGZFQpgQgAJBAS2VCCQBAgrhCEWeARAIiYKAAAEAApAAEBYLA4kkBKxIIAuIJoAACABAIIAChFJ2YAggDNlqrwZNoytMCwfMFz2mAZAEQRk5JsQAA.f_wACHwAAAAA; __spdt=3b5d9272cbf74d35b5d8480d48487110; _tt_enable_cookie=1; _ttp=XfWVeUWImhrbYUV3PXf3iTpsjtu.tt.1; _scid=FN13FfQRhjnl79qdjQ6f0QfiM5HRPmVb; _clck=wcusc2%7C2%7Cftr%7C0%7C1861; _sctr=1%7C1740502800000; OptanonConsent=isGpcEnabled=0&datestamp=Wed+Feb+26+2025+15%3A56%3A50+GMT%2B0700+(Indochina+Time)&version=202408.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=b10db874-e5dc-4d8e-a006-c30784fabda5&interactionCount=2&isAnonUser=1&landingPath=NotLandingPage&groups=C0003%3A1%2CC0004%3A1%2CC0002%3A1%2CC0005%3A1%2CC0001%3A1%2CV2STACK42%3A1&AwaitingReconsent=false&intType=1&geolocation=TH%3B10; _scid_r=Il13FfQRhjnl79qdjQ6f0QfiM5HRPmVbSPasFQ; _ga_0SXVVHPVKT=GS1.1.1740565117.10.1.1740567899.0.0.0; .AspNetCore.Cookies=; .AspNetCore.CookiesC1=; .AspNetCore.CookiesC2=; __gads=ID=086a1f2ff3b93b7f:T=1734147882:RT=1751793781:S=ALNI_MbFlc2epxawJb6dJV547TzESz7-nA; __gpi=UID=00000f8f0542ee95:T=1734147882:RT=1751793781:S=ALNI_MbAiIsaXVTFp768VcMdCz_PiGuX6A; __eoi=ID=733e6ae3a82970fc:T=1750819223:RT=1751793781:S=AA-AfjZbwA4hCTwYXsgJyxFQmalz; _ga_TIKTOK=GS2.1.s1751793780$o12$g0$t1751793780$j60$l0$h1856245207; _ga_FBMAIN=GS2.1.s1751793780$o12$g0$t1751793780$j60$l0$h1202007613; FPLC=Ggp5NRLF79rrZNHeu6dirieeJAfkQaGps7buGisVClqDpAzoogrYZkWQ9kefELgBUxz1Obo9hZ%2FqGIabiOEz6ic%2BkHIZH4Lf03PccknwDBNaVd5r8D0ta%2BVNxtcVTQ%3D%3D; __cmpcccu75435=aCQUJoT7AAqWAGQwiLUKYAA',
    }

    params = {
        'playerEntryId': '4pu8Vnba43JYreI7ytlXGR',
    }

    response = requests.get(
        'https://www.chelseafc.com/en/api/profiles/4pu8Vnba43JYreI7ytlXGR/stats',
        params=params,
        cookies=cookies,
        headers=headers,
    )
    print(response.status_code)
    chelsea = response.json()
    filename = "chelsea.json"

    save_data(chelsea,filename)

def save_data(data, filename):
    folder_path="/mnt/d/Football_data/chelsea_data/data"
    os.makedirs(folder_path, exist_ok=True)
    file_path = os.path.join(folder_path, filename)

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print(f"Saved data to {file_path}")

if __name__ == "__main__":
    scarping_chelsea()