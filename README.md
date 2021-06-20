# fastapi-jwt-skeleton
Skeleton for authentication &amp; authorization through JWT in FastAPI

##  How to start:
1. Install the files provided in `requirements.txt` with `pip install -r requirements.txt`
2. Create a `.env` file.
    1. Add the following content:
    ```env
   secret=please_please_update_me_please
   algorithm=HS256
   ```
   2. Change the `please_please_update_me_please` to something more random, for instance by using this:
   ```python
   >>> import os
   >>> import binascii
   >>> binascii.hexlify(os.urandom(24))
   b'deff1952d59f883ece260e8683fed21ab0ad9a53323eca4f'
   ```
3. Run by using `python main.py`
4. The server should be running on `localhost:8081/` and the documentation should be available through `localhost:8081/docs`
   
