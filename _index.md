---
type: Index
---
[[🔗 LINKS]]
[[_log]]

```dataviewjs

const notes = await dv.query (`
TABLE 
R.file.link as Note
FROM "💽 Backend/📖 DSC Handbook"
GROUP BY type
FLATTEN rows as R 
WHERE type != "Index"
SORT type
`)

console.log(notes)

if (!notes.successful) {
  dv.paragraph(`~~~~\n${ notes.error }\n~~~~\n`)
  return
}

let typeDict = {}
for (let note of notes.value.values) {
  if ( !typeDict.hasOwnProperty(note[0]) )
    typeDict[note[0]] = []

  typeDict[note[0]].push([...note.slice(1)])
}

for (let key of Object.keys(typeDict)) {
  dv.header(2, key)
  dv.table([...notes.value.headers.slice(1)],
    typeDict[key])
}
```
