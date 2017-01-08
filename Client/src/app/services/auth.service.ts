import { Injectable } from '@angular/core';
import { Http,Headers,Response } from '@angular/http';
import "rxjs"

@Injectable()

export class authService{

    constructor(private http:Http){}

    private headers=new Headers({'Content-Type':'application/json'});
    private signUpUrl="http://192.168.12.27:8000/api/signup";
    private loginUrl="http://192.168.12.27:8000/api/login";
    private signoutUrl="http://192.168.12.27:8000/api/signout"

    signUp(username:string,password:string,contact:number,firstName:string,lastName:string,emailId:string):Promise<any>{
        return this.http.post(this.signUpUrl,JSON.stringify({username:username,password:password,email_id:emailId,contact:contact,first_name:firstName,last_name:lastName}),{headers:this.headers})
        .toPromise()
        .then((res:Response) => {})
        .catch((err) => console.log("Error"))  
    }

    login(username:string,password:string):Promise<any>{
        return this.http.post(this.loginUrl,JSON.stringify({username:username,password:password}),{headers:this.headers})
        .toPromise()
        .then((res:Response) => {})
        .catch((err) => console.log("Error"))
    }

    signOut():Promise<any>{
        return this.http.get(this.signoutUrl, {headers:this.headers})
        .toPromise()
        .then((res:Response) => {})
        .catch((err) => console.log("Error"))
    }
} 
