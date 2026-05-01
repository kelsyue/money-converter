# GlobalScale Currency Utility

A Python-based currency converter featuring a Tkinter GUI.  
This project demonstrates version control hygiene, API integration, and AI-assisted development.

## Features
- Real-time currency conversion using exchange rate API  
- Simple Tkinter graphical interface  
- Secure API key management using environment variables  
- Basic CI testing via GitHub Actions  

## Setup
1. Ensure Python 3.11+ is installed.  
2. Install dependencies:
   ```
   pip install requests python-dotenv
   ```
3. Create a `.env` file and add your API key:
   ```
   EXCHANGE_RATE_API_KEY=your_api_key_here
   ```
4. Run `python gui.py` to start the application.

## Testing
Run the CI check locally:
```bash
python -c "from converter import convert_currency; assert convert_currency(1, 'USD', 'USD') == 1.0"
```

## Project Structure
```
converter.py   - Core conversion logic
gui.py         - Tkinter interface
.env           - API key (not tracked in git)
```
