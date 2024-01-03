# BibTitleCapitalizer

批量处理 bib 文件中的英文标题

API source: [Capitalize My Title API]( https://capitalizemytitle.com/api/ )


## Usage
- 在 [Capitalize My Title API | RapidAPI]( https://rapidapi.com/capitalize-my-title-cmt/api/capitalize-my-title ) 注册并申请 API
- 在 .env 文件中添加申请到的 API_Key：

    ```
    API_KEY=[YOUR KEY HERE]
    ```
- `python main.py`

## TODO
- [ ] 处理斜杠
- [ ] 文档
- [ ] 合并标题减少调用（探索最长限制）
- [ ] 尝试模拟浏览器点击
