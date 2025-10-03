#导入必需的库
import os
import requests
from rich.console import Console
from rich.table import Column, Table
from rich.prompt import Prompt, IntPrompt

#创建终端示例
console = Console()

#创建表格
table = Table(Column(header="检测时请不要开加速器！！！", justify="center"),
              show_header=True, 
              header_style="red",
              title = "[blue]清单下载器 V1.0[/blue]")
table.add_row("1. 下载单清单")
table.add_row("2. 下载多清单")

#循环开启
while True:
    #打印表格
    console.print(table)
    
    #询问下载方式
    choice = Prompt.ask("请选择下载方式", choices=["1", "2"], default="1")
    
    #判断选择
    if choice == "1":
        #下载单清单实现
        console.print("---***下载单清单***---")
        while True:
            list_number = IntPrompt.ask("请输入清单")
            if list_number:
                console.print("[green]开始检测[/green]...")
                try:
                    url = f"https://github.com/SteamAutoCracks/ManifestHub/archive/refs/heads/{list_number}.zip"
                    response = requests.get(url)
                    if response.status_code == 200:
                            console.print("[green]清单存在[/green]")
                            break
                    else:
                            console.print("[red]清单不存在[/red]")
                except Exception:
                    console.print("[red]请关闭加速器再试一次[/red]")
                    break            
            else:
                console.print("[red]输入错误，再试一次[/red]")
        os.system(f"aria2c -j 16 {url}")
        console.print(f"[green]清单{list_number}下载完成[/green]")
        break
    elif choice == "2":
        #下载多清单实现
        list_number_list = []
        console.print("---***下载多清单***---")
        while True:
            while True:
                list_number = IntPrompt.ask("请输入清单")
                if list_number:
                    list_number_list.append(list_number)
                    confirm = Prompt.ask("是否继续输入清单", choices=["y", "n"], default="y")
                    if confirm == "y":
                        continue
                    elif confirm == "n":
                        console.print("[green]开始检测[/green]...")
                        try:
                            for list_number in list_number_list:
                                url = f"https://github.com/SteamAutoCracks/ManifestHub/archive/refs/heads/{list_number}.zip"
                                response = requests.get(url)
                                if response.status_code == 200:
                                    console.print(f"[green]清单{list_number}存在[/green]")
                                else:
                                    console.print(f"[red]清单{list_number}不存在[/red]")
                                    list_number_list.remove(list_number)
                                    console.print(f"[red]清单{list_number}已从列表中移除[/red]")
                            break
                        except Exception:
                            console.print("[red]请关闭加速器再试一次[/red]")
                            break
                    else:
                        console.print("[red]输入错误，再试一次[/red]")
                else:
                    console.print("[red]输入错误，再试一次[/red]")
            for list_number in list_number_list:
                url = f"https://github.com/SteamAutoCracks/ManifestHub/archive/refs/heads/{list_number}.zip "  
                os.system(f"aria2c -j 16 {url}")
                console.print(f"[green]清单{list_number}下载完成[/green]")
            break
