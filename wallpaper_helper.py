import os
import random
import ctypes
import requests
from tkinter import Tk, Button, Label, Frame, Entry, messagebox
from tkinter.filedialog import askdirectory
from PIL import Image, ImageTk
import tempfile

class WallpaperHelper:
    def __init__(self, master):
        self.master = master
        self.master.title("随机壁纸助手")
        self.master.geometry("400x300")
        self.master.resizable(False, False)
        
        # 本地壁纸文件夹路径
        self.local_folder = ""
        
        # 在线壁纸API（使用Picsum Photos API）
        self.unsplash_api = "https://picsum.photos/1920/1080"
        
        # 创建UI
        self.create_ui()
    
    def create_ui(self):
        # 主框架
        main_frame = Frame(self.master, padx=20, pady=20)
        main_frame.pack(fill="both", expand=True)
        
        # 标题
        title_label = Label(main_frame, text="随机壁纸助手", font=("Arial", 16, "bold"))
        title_label.pack(pady=10)
        
        # 本地文件夹选择
        folder_frame = Frame(main_frame)
        folder_frame.pack(fill="x", pady=10)
        
        folder_label = Label(folder_frame, text="本地壁纸文件夹:")
        folder_label.pack(side="left", padx=5)
        
        self.folder_entry = Entry(folder_frame, width=30)
        self.folder_entry.pack(side="left", padx=5, fill="x", expand=True)
        
        browse_button = Button(folder_frame, text="浏览", command=self.browse_folder)
        browse_button.pack(side="right", padx=5)
        
        # 操作按钮
        button_frame = Frame(main_frame)
        button_frame.pack(fill="x", pady=20)
        
        local_button = Button(button_frame, text="从本地随机设置", command=self.set_local_wallpaper, width=15)
        local_button.pack(side="left", padx=10)
        
        online_button = Button(button_frame, text="从在线随机设置", command=self.set_online_wallpaper, width=15)
        online_button.pack(side="right", padx=10)
        
        # 状态标签
        self.status_label = Label(main_frame, text="就绪", fg="green")
        self.status_label.pack(pady=10)
    
    def browse_folder(self):
        folder = askdirectory(title="选择壁纸文件夹")
        if folder:
            self.local_folder = folder
            self.folder_entry.delete(0, "end")
            self.folder_entry.insert(0, folder)
    
    def get_image_files(self, folder):
        """获取文件夹中的图片文件"""
        image_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.gif']
        image_files = []
        
        for root, _, files in os.walk(folder):
            for file in files:
                if any(file.lower().endswith(ext) for ext in image_extensions):
                    image_files.append(os.path.join(root, file))
        
        return image_files
    
    def set_wallpaper(self, image_path):
        """设置壁纸"""
        try:
            # Windows系统
            if os.name == 'nt':
                ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)
            # macOS系统
            elif os.name == 'posix' and 'darwin' in os.uname().sysname.lower():
                os.system(f"osascript -e 'tell application \"Finder\" to set desktop picture to POSIX file \"{image_path}\"'")
            # Linux系统
            elif os.name == 'posix':
                # 尝试多种Linux桌面环境的壁纸设置命令
                desktop_env = os.environ.get('XDG_CURRENT_DESKTOP', '')
                if 'gnome' in desktop_env.lower():
                    os.system(f"gsettings set org.gnome.desktop.background picture-uri file://{image_path}")
                elif 'kde' in desktop_env.lower():
                    os.system(f"qdbus org.kde.plasmashell /PlasmaShell org.kde.PlasmaShell.evaluateScript 'var allDesktops = desktops();print(allDesktops);for (i=0;i<allDesktops.length;i++) {{d = allDesktops[i];d.wallpaperPlugin = \"org.kde.image\";d.currentConfigGroup = Array(\"Wallpaper\", \"org.kde.image\", \"General\");d.writeConfig(\"Image\", \"file://{image_path}\");}}'")
                else:
                    # 通用Linux命令
                    os.system(f"feh --bg-scale {image_path}")
            
            self.status_label.config(text="壁纸设置成功！", fg="green")
            messagebox.showinfo("成功", "壁纸设置成功！")
        except Exception as e:
            self.status_label.config(text=f"设置失败: {str(e)}", fg="red")
            messagebox.showerror("错误", f"设置壁纸失败: {str(e)}")
    
    def set_local_wallpaper(self):
        """从本地文件夹随机设置壁纸"""
        if not self.local_folder:
            messagebox.showwarning("警告", "请先选择本地壁纸文件夹！")
            return
        
        try:
            image_files = self.get_image_files(self.local_folder)
            if not image_files:
                messagebox.showinfo("提示", "所选文件夹中没有找到图片文件！")
                return
            
            # 随机选择一张图片
            selected_image = random.choice(image_files)
            self.set_wallpaper(selected_image)
        except Exception as e:
            self.status_label.config(text=f"错误: {str(e)}", fg="red")
            messagebox.showerror("错误", f"设置本地壁纸失败: {str(e)}")
    
    def set_online_wallpaper(self):
        """从在线随机获取并设置壁纸"""
        try:
            self.status_label.config(text="正在下载壁纸...", fg="blue")
            self.master.update()
            
            # 下载随机壁纸
            response = requests.get(self.unsplash_api, timeout=10)
            response.raise_for_status()
            
            # 保存到临时文件
            with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as temp_file:
                temp_file.write(response.content)
                temp_file_path = temp_file.name
            
            # 设置壁纸
            self.set_wallpaper(temp_file_path)
            
            # 注意：临时文件不会被自动删除，以便壁纸可以正常显示
        except Exception as e:
            self.status_label.config(text=f"错误: {str(e)}", fg="red")
            messagebox.showerror("错误", f"获取在线壁纸失败: {str(e)}")

if __name__ == "__main__":
    root = Tk()
    app = WallpaperHelper(root)
    root.mainloop()
