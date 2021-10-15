mkdir -p ~/.streamlit/

echo "[general]
email = lpr.cid20@uea.edu.br
" > ~/.streamlit/credentials.toml

echo "[server]
headless = true
enableCORS = false
port = $PORT
" > ~/.streamlit/config.toml