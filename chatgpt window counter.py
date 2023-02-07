import win32gui

def get_window_titles():
    def callback(hwnd, window_titles):
        if win32gui.IsWindowVisible(hwnd):
            window_titles.append(win32gui.GetWindowText(hwnd))
        return True
    
    window_titles = []
    win32gui.EnumWindows(callback, window_titles)
    return window_titles

# get the list of window titles
window_titles = get_window_titles()

# count the number of windows
num_windows = len(window_titles)

print(f"Number of open windows: {num_windows}")






