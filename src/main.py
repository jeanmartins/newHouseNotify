import json
import os
import time
from types import SimpleNamespace
import requests
from winotify import Notification, audio


def run_Toaster(total):
    toaster = Notification(app_id="house-notify", title="House Notifier",
                           msg="Total Houses: " + str(total), duration="short",
                           icon=os.path.abspath("./image/house.ico"))
    toaster.add_actions("Check Here!", "https://www.torresdemeloneto.com.br/aluguel/casa/fortaleza/")
    toaster.set_audio(audio.Default, loop=False)
    toaster.show()


if __name__ == '__main__':

    Headers = {
        "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IlRva2VuIEFQSSIsImJ1c2luZXNzIjoiVG9ycmVzIGRlIE1lbG8gTmV0byIsImlhdCI6MTUxNjIzOTAyMn0.MSx_rDRMztOYOSN3VVjg89YtxC5wtoGQHqGEUvFRcpU"}
    apiUrl = "https://api.torresdemeloneto.com.br/v1/aluguel/imoveis?limit=500&offset=0&tipo=casa&endereco=fortaleza"
    totalHouses = 0
    totalHousesNow = 0
    while True:
        request = requests.get(apiUrl, headers=Headers)
        torresResponse = json.loads(request.text, object_hook=lambda d: SimpleNamespace(**d))
        totalHousesNow = int(torresResponse.resultado.total)
        if totalHousesNow > totalHouses or totalHousesNow < totalHouses or totalHouses == 0:
            totalHouses = totalHousesNow
            run_Toaster(totalHouses)
        time.sleep(300)
