
---

```dataviewjs

for (let page of dv.pages('"📝 Journal"').sort(p => p.file.name, 'desc')) {
  // Clickable heading linking to the note
  dv.header(2, page.file.link);              

  // Load and display the note's full content
  let content = await dv.io.load(page.file.path);  
  dv.paragraph(content);                     
}

```
