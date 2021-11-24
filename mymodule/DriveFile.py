# encoding: utf-8

# library
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

directorio_credenciales = 'credentials_module.json'

# class JSON
class DriveFile:
    def __init__(self, credentialsFile: str):
        # declare variables
        self.credentialsFile = credentialsFile

    def login(self):
        GoogleAuth.DEFAULT_SETTINGS['client_config_file'] = self.credentialsFile
        gauth = GoogleAuth()
        gauth.LoadCredentialsFile(self.credentialsFile)

        if gauth.credentials is None:
            gauth.LocalWebserverAuth(port_numbers=[8092])
        elif gauth.access_token_expired:
            gauth.Refresh()
        else:
            gauth.Authorize()

        gauth.SaveCredentialsFile(self.credentialsFile)
        credentials = GoogleDrive(gauth)
        return credentials

    def searchFile(self, query, mode: str):
        credentials = self.login()
        resultado = []
        lista_archivos = credentials.ListFile({'q': query}).GetList()
        for f in lista_archivos:

            if mode == 'link':
                resultado.append({"title": f['title'], "id": f['id'], "link": f['embedLink']})
            else:
                resultado.append({f})
        return resultado

    def uploadFile(self, rutaFile: str, id_folder: str):
        credentials = self.login()
        file = credentials.CreateFile({'parents': [{"kind": "drive#fileLink",
                                                    "id": id_folder}]})
        file['title'] = rutaFile.split("\\")[-1]
        name = file['title']
        file.SetContentFile(rutaFile)
        file.Upload()
        return name

    def deleteFile(self, fileID: str):
        credentials = self.login()
        file = credentials.CreateFile({'id': fileID})
        # delete file
        file.Delete()
