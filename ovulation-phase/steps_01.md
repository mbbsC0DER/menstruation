# Practical 01 — Express and MongoDB

## Before starting

- Install Node.js/npm and MongoDB Community Server. MongoDB Compass alone is not the database server.
- Start your local MongoDB server on `127.0.0.1:27017`.
- Open a terminal in `ovulation-phase`. The code files are already provided.
- Run one practical at a time: both servers use port `3000`.

## 1a — CRUD operations

1. Set up and start the server:

   ```bash
   cd crud_1a
   npm init -y
   npm install express mongoose
   node server.js
   ```

2. Wait for `MongoDB connected`. Keep this terminal running.
3. Open Postman and create a user:
   - Method: `POST`
   - URL: `http://localhost:3000/users`
   - Body: **raw → JSON**

   ```json
   { "name": "Amit", "age": 21, "email": "amit@example.com" }
   ```

4. Copy the returned `_id`. Replace `USER_ID` below with that value.

   | Operation | Method | URL | JSON body |
   |---|---|---|---|
   | Read all | GET | `http://localhost:3000/users` | None |
   | Read one | GET | `http://localhost:3000/users/USER_ID` | None |
   | Update | PUT | `http://localhost:3000/users/USER_ID` | `{"age":22}` |
   | Delete | DELETE | `http://localhost:3000/users/USER_ID` | None |

5. Read the user after updating to verify the new age. Read all after deleting to verify removal.
6. In MongoDB Compass, connect to `mongodb://127.0.0.1:27017` and inspect **studentDB → users**. The database appears after the first successful insert.
7. Press **Ctrl+C** in the server terminal before starting 1b.

## 1b — Upload an image or document

1. From the `crud_1a` terminal, set up and start the upload server:

   ```bash
   cd ../upload_1b
   npm init -y
   npm install express mongoose multer
   node server.js
   ```

   If using a fresh terminal in `ovulation-phase`, use `cd upload_1b` instead.

2. Wait for `MongoDB connected`.
3. In Postman:
   - Method: `POST`
   - URL: `http://localhost:3000/files/upload`
   - Body: **form-data**
   - Add key **file**, change its type from **Text** to **File**, and select a small image or document.
   - Click **Send**. Let Postman set the multipart Content-Type automatically.
4. Copy the returned `id` and open `http://localhost:3000/files/FILE_ID`, replacing `FILE_ID`. The browser displays or downloads the file according to its type.
5. In Compass, inspect **fileDB → files**. The document contains the filename, content type, and binary data.
6. Press **Ctrl+C** to stop the server.

## If something fails

- **Connection refused on port 27017:** start MongoDB and confirm its address matches the code.
- **Port 3000 already in use:** stop the other practical's server first.
- **No file uploaded:** use form-data with the exact key `file` and select a file.
- **Cannot find module:** run the relevant `npm install` command inside that practical's folder.
