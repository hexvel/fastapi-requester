import json
import aiohttp
import asyncio


class Request:
    def __init__(self):
        self.success: bool = None
        self.data: dict = None
        self.url = "http://127.0.0.1:8000"

    async def __request(self, params: dict) -> dict:
        """Database query.

        Args:
            params (dict): parameters for creating a record in the database.

        Returns:
            dict: Database query result
        """

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(self.url, params=params) as resp:
                    return await resp.json()
        except Exception as error:
            return {"success": False, "data": str(error)}

    async def create(self, *, filters: dict, params: dict):
        """Creating a new record in the database.

        Args:
            filters (dict): search filters
            params (dict): parameters for creating a record in the database.

        Returns:
            dict: Database query result
        """

        data = dict(filters=json.dumps(filters), params=json.dumps(params))
        self.url += "/create"
        request = await self.__request(data)
        self.success = request["success"]
        self.data = request["data"]

        return self

    async def update(self, *, filters: dict, params: dict):
        """Update a record in the database.

        Args:
            filters (dict): search filters
            params (dict): parameters for updating a record in the database.

        Returns:
            dict: Database query result
        """

        data = dict(filters=json.dumps(filters), params=json.dumps(params))
        self.url += "/update"
        request = await self.__request(data)

        self.success = request["success"]
        self.data = request["data"]

        return self

    async def delete(self, *, filters: dict):
        """Update a record in the database.

        Args:
            filters (dict): search filters
            params (dict): parameters for updating a record in the database.

        Returns:
            dict: Database query result
        """

        data = dict(filters=json.dumps(filters))
        self.url += "/delete"
        request = await self.__request(data)

        self.success = request["success"]
        self.data = request["data"]

        return self

    async def get(self, *, filters: dict):
        """Get a record in the database.

        Args:
            filters (dict): search filters

        Returns:
            self
        """

        data = dict(filters=json.dumps(filters))
        self.url += "/get"
        request = await self.__request(data)
        self.success = request["success"]
        self.data = request["data"]

        return self
