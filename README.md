# projectime

Keep track of task time basd on Django


## Weekly Report API

### Get Projects

#### URL
    HTTP GET /projects

#### Response
##### Success
 - `Code`: 200
 - `Content`:
```json
// JSON
[
// project 1
{
    project_id:[string]      // project id
    project_name: [string]   // project name
}

// project 2
{
    project_id:[string]      // project id
    project_name: [string]   // project name
}

// project 3
...
]
```
----

### Get Records 

#### URL
    HTTP GET /records

#### URL Params
- `from` [date]  
    the date when record start from
- `to` [date]  
    the date when record ends to
- `userid` [string]  
    the user of the query record

#### Response

##### Success
- `Code`: 200  
- `Content`:  
```json
// JSON
[

// record 1
{
user:[string]    // user id
project:[string] // project id
date:[string]    // ISO format date
hour:[int]       // hour
},

// record 2
{
user:[string]    // user id
project:[string] // project id
date:[string]    // ISO format date
hour:[int]       // hour
}

// record 3
...
]
```
----

### Add Records
#### URL
    HTTP POST /records

#### Data Params
```json
// JSON
[

// record 1
{
user:[string]    // user id
project:[string] // project id
date:[string]    // ISO format date
hour:[int]       // hour
},

// record 2
{
user:[string]    // user id
project:[string] // project id
date:[string]    // ISO format date
hour:[int]       // hour
}

// record 3
...
]
```

#### Response
##### Success
- `Code`: 200  

----
