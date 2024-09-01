#!/usr/bin/env python3
# sql_injection_gui.py

import tkinter as tk
from tkinter import ttk, messagebox
import requests
from payloads import payloads  # Importing the payloads from payloads.py

def send_requests(url, param):
    results = []
    for payload in payloads:
        payload_url = f"{url}?{param}={payload}"
        try:
            response = requests.get(payload_url, timeout=5)  # Added timeout
            if is_vulnerable(response):
                results.append(payload_url)
        except requests.exceptions.RequestException as e:
            # Handle connection errors and print the error for debugging
            print(f"Error with URL {payload_url}: {e}")
    return results

def is_vulnerable(response):
    error_messages = ["sql syntax", "sql error", "database error", "unclosed quotation mark", "sql state"]
    for error in error_messages:
        if error in response.text.lower():
            return True
    return False

def start_scan():
    url = url_entry.get()
    param = param_entry.get()
    if not url or not param:
        messagebox.showwarning("Input Error", "Please provide both URL and parameter.")
        return

    results = send_requests(url, param)
    if results:
        result_text = "The following URLs are potentially vulnerable to SQL Injection:\n\n" + "\n".join(results)
    else:
        result_text = "No SQL Injection vulnerabilities found."

    result_box.delete(1.0, tk.END)
    result_box.insert(tk.END, result_text)

# Create main application window
root = tk.Tk()
root.title("SQL Injection Automation Tool")
root.geometry("600x400")

# Create and place the components
ttk.Label(root, text="URL:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
url_entry = ttk.Entry(root, width=50)
url_entry.grid(row=0, column=1, padx=10, pady=10)

ttk.Label(root, text="Parameter:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
param_entry = ttk.Entry(root, width=50)
param_entry.grid(row=1, column=1, padx=10, pady=10)

scan_button = ttk.Button(root, text="Start Scan", command=start_scan)
scan_button.grid(row=2, column=0, columnspan=2, padx=10, pady=20)

result_box = tk.Text(root, wrap="word", height=10, width=70)
result_box.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Start the GUI event loop
root.mainloop()
