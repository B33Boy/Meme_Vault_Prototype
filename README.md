### USAGE

#### Make sure that pytesseract is installed 
Ubuntu: `sudo apt-get install tesseract-ocr`


#### Run Application:
`cd Meme_Vault_Prototype/` \
Linux: `./start.sh`  or Windows: `start.sh`

#### Database Migrations
`flask db migrate -m "SCHEMA_CHANGE_MESSAGE" ` \
`flask db upgrade`
