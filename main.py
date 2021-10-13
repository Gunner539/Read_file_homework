
import requests
import os

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {'Content-Type': 'application/json', 'Authorization': 'OAuth {}'.format(self.token)}


    def _get_upload_link(self, file_path):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': file_path, 'overwrite': 'true'}
        response = requests.get(url=upload_url, headers=headers, params=params)
        return response.json()


    def upload(self, file_path: str):
        href = self._get_upload_link(file_path).get('href', '')
        filename = os.path.basename(file_path)
        response = requests.put(url=href, data=open(filename, 'rb'))
        response.raise_for_status()



if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = '...'
    token = '...'
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)

