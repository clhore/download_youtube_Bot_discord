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
        # Archivos con el nombre 'mooncode': title = 'mooncode'
        # Archivos que contengan 'mooncode' y 'mooncoders': title contains 'mooncode' and title contains 'mooncoders'
        # Archivos que NO contengan 'mooncode': not title contains 'mooncode'
        # Archivos que contengan 'mooncode' dentro del archivo: fullText contains 'mooncode'
        # Archivos en el basurero: trashed=true
        # Archivos que se llamen 'mooncode' y no esten en el basurero: title = 'mooncode' and trashed = false
        lista_archivos = credentials.ListFile({'q': query}).GetList()
        for f in lista_archivos:
            # ID Drive
            print('ID Drive:', f['id'])
            # Link de visualizacion embebido
            print('Link de visualizacion embebido:', f['embedLink'])
            # Nombre del archivo
            print('Nombre del archivo:', f['title'])
            # Tipo de archivo
            print('Tipo de archivo:', f['mimeType'])
            # Esta en el basurero
            print('Esta en el basurero:', f['labels']['trashed'])
            # Fecha de creacion
            print('Fecha de creacion:', f['createdDate'])
            # Fecha de ultima modificacion
            print('Fecha de ultima modificacion:', f['modifiedDate'])
            # Version
            print('Version:', f['version'])
            # Tamanio
            print('Tamanio:', f['fileSize'])
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