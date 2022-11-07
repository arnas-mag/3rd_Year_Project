import mysql from 'mysql';
/*Change connection details for actual project*/
const connection = mysql.createConnection({
    host: 'localhost',
    user:'root',
    password:'',
    database:'group_project',
});
/*Stays the same*/
export const db = {
    connect:()=> connection.connect(),
    query:(queryString, escapedValues)=>
    new Promise((resolve, reject)=>{
        connection.query(queryString, escapedValues, (error, results, fields)=>{
            resolve({results, fields});
        })
    }),
    end:()=>connection.end(),
}