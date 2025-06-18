from tkinter import Tk, Label, Entry, Button
from tkinter import filedialog

from crawler import get_youtube_comments

def shorten_path(path, max_len=38) :
    return path if len(path) <= max_len else "..." + path[-(max_len - 3):]

class YouTubeCommentCrawler:
    def __init__(self, root):
        self.root = root
        root.title("유튜브 댓글 저장기")

        root.update_idletasks()
        root.minsize(width=500, height=0)

        self.selected_folder = "저장 경로를 설정해주세요"

        Label(root, text='유튜브 URL').grid(row=0, column=0, sticky="w", padx=10, pady=(10, 5))
        self.url_entry = Entry(root)
        # self.url_entry.insert(0, "URL 입력")
        self.url_entry.grid(row=1, column=0, columnspan=2, sticky="ew", padx=10)

        Label(root, text="저장 위치").grid(row=2, column=0, sticky="w", padx=10, pady=(15, 0))
        self.path_label = Label(root, text=shorten_path(self.selected_folder), fg='gray')
        self.path_label.grid(row=3, column=0, sticky="w", padx=10)

        self.change_button = Button(root, text="변경", width=10, command=self.choose_folder)
        self.change_button.grid(row=3, column=1, sticky="e", padx=10, pady=5)

        self.start_button = Button(root, text="시작", width=10, command=lambda: get_youtube_comments(self.url_entry.get(), self.selected_folder))
        self.start_button.grid(row=4, column=1, sticky="e", padx=10, pady=5)

        root.columnconfigure(0, weight=1)

    def choose_folder(self):
        folder = filedialog.askdirectory()
        if not folder:
            return
        
        self.selected_folder = folder
        self.path_label.config(text=f"{shorten_path(self.selected_folder)}")

if __name__ == "__main__":
    root = Tk()
    app = YouTubeCommentCrawler(root)
    root.mainloop()
