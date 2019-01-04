# projectime
a django project


# Weekly Report API


### Get projects

### Get records 

### URL
**HTTP GET /records**

#### URL Params
- `from` = [date] 
- `to` = [date]
- `userid` = [string]

## Add records
### URL
    HTTP POST /records
### Data Params
JSON
```json
[
{
user:[string]    // user id
project:[string] // project id
date:[string]    // ISO format date
hour:[int]       // hour
},

{
user:[string]    // user id
project:[string] // project id
date:[string]    // ISO format date
hour:[int]       // hour
}

...
]
```
