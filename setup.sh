mkdir -p ~/.streamlit/

echo "[theme]
primaryColor="#3872fb"
backgroundColor="#0e1117"
secondaryBackgroundColor="#333c4f"
textColor="#fafafa"
font="sans serif"
[server]
headless = true
port = $PORT
enableCORS = false
" > ~/.streamlit/config.toml