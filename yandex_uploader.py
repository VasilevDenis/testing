import requests
import secret


class YaUploader:
    def __init__(self, token: str):
        self.token = token
        self.url = 'https://cloud-api.yandex.net/'

    def upload_file_to_disk(self, disk_file_path, filename):
        href_response = self._get_upload_link(disk_file_path=disk_file_path)
        href = href_response.get('href', '')
        response = requests.put(url=href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print('Success')

    def create_folder(self, folder):
        url = f'{self.url}v1/disk/resources?path={folder}'
        headers = self._get_headers()
        response = requests.put(url, headers=headers)
        return response.status_code

    def check_folder(self, folder):
        url = f'{self.url}v1/disk/resources?path={folder}'
        headers = self._get_headers()
        response = requests.get(url, headers=headers)
        return response.status_code

    def _get_headers(self):
        return {'Content-Type': 'application/json', 'Authorization': f'OAuth {self.token}'}

    def _get_upload_link(self, disk_file_path):
        upload_url = f'{self.url}v1/disk/resources/upload'
        headers = self._get_headers()
        params = {'path': disk_file_path, 'overwrite': 'true'}
        href_response = requests.get(upload_url, headers=headers, params=params)
        return href_response.json()


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = 'questions.txt'
    uploader = YaUploader(secret.token)
    folder_path = 'test2'
    upload_status = uploader.create_folder(folder_path)
    print(upload_status)
    check_status = uploader.check_folder(folder_path)
    print(check_status)


