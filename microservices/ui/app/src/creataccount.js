import React from 'react';
import styled from 'styled-components'
import {elementById, takeToHome} from './module'
import {config} from './config'

const Pannel =styled.div`
  width: 100%;
  height: 100%;
`;
const Navbar = styled.div`
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: flex-start;
  position: relative;
  height: 90px;
  background: #fff;
  border: 1px solid #0000001a;
`;
const TinderLogo = styled.div`
 width: 150px;
 margin-left: 6%;
`;
const H3 = styled.div`
      font-style: italic;
      font-weight: bolder;
      font-size: x-large;
      font-weight: 753px;
      line-height: 2.em;
      text-transform: uppercase;
      word-wrap: break-word;
      text-align: center;
      margin-top: 50px;
      margin-bottom: 30px;
`;
const Textarea = styled.textarea`
  width: 300px;;
  padding: 0.8em;
  border: 1px solid #eaeaea;
  background-color: #efefef;
  cursor: text;
  box-sizing: border-box;
  border-radius: 5px;
  color: #555;
  font-weight: 700;
  line-height: 1.2em;
  font-size: initial;
  display: block;
  margin: 20px;
  &:focus{
    background: white;
    outline: 0;
    border: 2px solid #465867;
  }
`;
const Input = styled.input`
  width: 300px;;
  padding: 0.8em;
  border: 1px solid #eaeaea;
  background-color: #efefef;
  cursor: text;
  box-sizing: border-box;
  border-radius: 5px;
  color: #555;
  font-weight: 700;
  line-height: 1.2em;
  font-size: initial;
  display: block;
  margin: 20px;
  &:focus{
    background: white;
    outline: 0;
    border: 2px solid #465867;
  }
`;
const MainContent = styled.div`
  display: flex;
  align-items: center;
  justify-content: center;
`;
const BtnContinue = styled.button`
    padding: 10px 42px;
    border-radius: 10px;
    background: #e12525;
    color: #fff;
    border: 1px solid aliceblue;
    margin-left: 84px;
`;
export class Acreacte extends React.Component{

// handle account creation doing some validte input and store on server
  handleAc(){
          const name = elementById('name').value;
          const email = elementById('email').value;
          const gender = elementById('gender').value;
          const age = elementById('age').value;
          const about = elementById('about').value;
          const city = elementById('city').value;
          const file = elementById('photo')
          const btnContinue = elementById('continue');
          btnContinue.innerHTML = 'Sending ...'
          //validating input here and upload to server
           uploadUserDetail(name,email,gender,file,age,about,city);
         //if response is treu the put user to home  call taketohome mnthod
          setTimeout(50);// waiting to uploading...here

  }
  //  <input type="file" style={{display:"none"}} id="inputfile"/>}
  render(){
    return (
      <Pannel>
        <Navbar>
          <TinderLogo>
                <img src={config.icons.tinderNameLogo} style={{height: 90}}/>
            </TinderLogo>
        </Navbar>
        <MainContent>
          <div style={{display: "block"}}>
            <H3>CREATE ACCOUNt</H3>
            <Input id="name" placeholder="First Name" type="text" />
            <Input id="email" placeholder="Email" type="email" />
            <Input id="gender" placeholder="Gender" type="text" />
            <Input id="age" placeholder="Age" type="text" />
            <Input id="city" placeholder="city" type="text" />
            <Textarea id="about" rows="4" cols="50" placeholder="about me" wrap="hard">
              </Textarea>
            <Input id="photo"  type="file" />
            <BtnContinue id="continue"
             onClick={this.handleAc}
              >Continue</BtnContinue>
          </div>
        </MainContent>
      </Pannel>
    );
  }
}


function uploadUserDetail(name,email,gender,file,age,about,city)
{
  // some AJAX api and using other to upload file
  // there is some AJAX call to put data to server
  // profile uploading file
  var url =  config.url.file;
  let file_id;
  let userDetails;
  // This is the file we are going to upload, replace this with your file
  // If you have the auth token saved in offline storage
   var authToken = window.localStorage.getItem('HASURA_AUTH_TOKEN');
  // headers = { "Authorization" : "Bearer " + authToken }
  var requestOptions = {
  	method: 'POST',
  	headers: {
        "Authorization": "Bearer " + authToken
  	},
  	body: file.files[0]
  }

  fetch(url, requestOptions)
  .then(function(response) {
  	return response.json();
  })
  .then(function(result) {
  	//console.log(result);
    // when Sucess fully return true
    userDetails = result;
    insertUser(result,name,email,gender,age,about,city)
  })
  .catch(function(error) {
  	console.log('Request Failed:' + error);
    alert('something went wrong please try again...')
  });

  // now we hav profile id put it on user details user table.ok
}

function insertUser(userDetails,name,email,gender,age,about,city){

  // normal user can not insert but foor now we can add admoin auth.
  var url = config.url.insert_user;
  // If you have the auth token saved in offline storage
   var authToken = window.localStorage.getItem('HASURA_AUTH_TOKEN');
  // headers = { "Authorization" : "Bearer " + authToken }
  var requestOptions = {
      "method": "POST",
      "headers": {
          "Content-Type": "application/json",
          "Authorization":" Bearer "+authToken
      }
  };

  var body = {
            "name": name,
            "email": email,
            "gender": gender,
            "file_id": userDetails.file_id,
            "age":age,
            "about_me": about,
            "city": city
  };

  requestOptions.body = JSON.stringify(body);

  fetch(url, requestOptions)
  .then(function(response) {
  	return response.json();
  })
  .then(function(results) {
  //	console.log(results);
    if(results.code!=="parse-failed"){
      let r ={
        hasura_id: userDetails.user_id,
      }
    takeToHome(r);
  }else{
    alert("something went wrong please try again");
  }
  })
  .catch(function(error) {
  	console.log('Request Failed:' + error);
  });
}
