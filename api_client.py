import requests


class CourierAPIClient:
    """
    Клиент для работы с API курьеров.
    Инкапсулирует логику запросов и авторизации.
    """

    def __init__(self, base_url: str, auth_token: str):
        # Сохраняем переданные параметры в атрибуты объекта
        self.base_url = base_url
        self.auth_token = auth_token

    def _get_auth_header(self) -> dict:
        """Приватный метод для формирования заголовка авторизации."""
        if not self.auth_token:
            raise ValueError("AUTH_TOKEN не задан")
        return {"Authorization": f"Bearer {self.auth_token}"}

    def get_courier_by_id(self, courier_id: int) -> dict:
        """Получает данные курьера по ID."""
        url = f"{self.base_url}/couriers/{courier_id}"
        headers = self._get_auth_header()
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

    def create_courier(self, data: dict) -> dict:
        """Создаёт нового курьера."""
        url = f"{self.base_url}/couriers"
        headers = self._get_auth_header()
        # Добавляем Content-Type, так как отправляем JSON
        headers["Content-Type"] = "application/json"
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()

    def delete_courier(self, courier_id: int) -> dict:
        """Удаляет курьера по ID."""
        url = f"{self.base_url}/couriers/{courier_id}"
        headers = self._get_auth_header()
        response = requests.delete(url, headers=headers)
        response.raise_for_status()
        return response.json()