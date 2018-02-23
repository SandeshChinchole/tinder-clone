import React from 'react';
import styled from 'styled-components';
import ReactDOM from 'react-dom';
import {Drover} from './home'
import { Acreacte} from './creataccount.js'
import {config} from './config'


// components here
const Input = styled.input`
  padding: 0.6em;
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
  margin: 0 auto;
  margin-top: 15px;
  padding-bottom: 4px;
  width: 63%;
  &:focus{
    background: white;
    box-shadow: 0px 0px 9px 0px #e20f0fbf;
    outline: 0;
    border: 0.5px solid #ec6e56;
  }
`;
const Button = styled.button`
    padding: 10px 38px;
    background: -moz-repeating-radial-gradient;
    border: 1px solid aliceblue;
    border-radius: 6px;
    color: white;
    background: #fe5068;
    font-weight: bold;
    &:focus {
    outline: 0;
    }
`;

const TinderLogo = styled.div`
  display: flex;
  justify-content: center;
  margin-top: 50px;
`;
const P = styled.p`
  font-size: 1.5em;
  text-transform: uppercase;
  font-style: italic;
  font-weight: bold;
  text-align: center;
  margin-top: 20px;
  margin-bottom: 60px;
  `;
const ButtonContainer = styled.div`
  display: flex;
  justify-content: center;
   margin-top: 18px;
`;
// get the element by Id ..
export function elementById(id){
  return document.getElementById(id);
}

function validatInput(username,password){
  return (username !== "") ? (password !== "") ? "true"  : "false" : "false";
}

//<Drover></Drover>
export function takeToHome(result){
  const curentU = result.hasura_id;
  let p;
  var url = config.url.getUsersInfo;

  // If you have the auth token saved in offline storage
   var authToken = window.localStorage.getItem('HASURA_AUTH_TOKEN');
  // headers = { "Authorization" : "Bearer " + authToken }
  var requestOptions = {
      "method": "GET",
      "headers": {
          "Authorization": "Bearer "+authToken
      }
  };

  fetch(url, requestOptions)
  .then(function(response) {
   return response.json();
  })
  .then(function(result) {
   if(result.message !== 'Select request failed'){
      result.map( s =>{if(s.hasura_id === curentU ){ p = s;} });
         if(!p){
           takeToAccountCreate();
         }
         else{
           const r = (
             <div>
               <Drover logedUser={p} id={curentU} userInfo={result}></Drover>
             </div>
           );
           ReactDOM.render(r,document.getElementById('root'));
         }
   }else{
     alert("something went wrong please try again!")
   }
  })
  .catch(function(error) {
   console.log('Request Failed:' + error);
    alert('something went wrong')
  });
}

export function takeToAccountCreate(result){

  const r = (
    <div>
      <Acreacte></Acreacte>
    </div>
  );
  ReactDOM.render(r,document.getElementById('root'));
}

/*
  login with the username & password
*/
function login(username,password){

    var url = config.url.login;

    var requestOptions = {
        "method": "POST",
        "headers": {
            "Content-Type": "application/json"
        }
    };

    var body = {
        "provider": "username",
        "data": {
            "username": username,
            "password": password
        }
    };

    requestOptions.body = JSON.stringify(body);

    fetch(url, requestOptions)
    .then(function(response) {
    	return response.json();
    })
    .then(function(result) {
      if(result.detail ===null){
        let BtnLogin = elementById('login');
        BtnLogin.innerHTML = "login";
        alert('username & password are incorrect');
      }
      else{
      	// To save the auth token received to offline storage
       var authToken = result.auth_token
       window.localStorage.setItem('HASURA_AUTH_TOKEN', authToken);
        window.localStorage.setItem('C_ID', result.hasura_id);
       takeToHome(result)
      }
    })
    .catch(function(error) {
    	console.log('Request Failed:' + error);
      let BtnLogin = elementById('login');
      BtnLogin.innerHTML = "login";
      alert('something went wrong please try again');
    });
}


// pack  the login and sign screen in one component here
export class Login extends React.Component{
  handleLogin(){
    let InputUser = elementById('username').value;
    let InputPassword = elementById('password').value;
    if(validatInput(InputUser,InputPassword) === 'true'){
      let BtnLogin = elementById('login');
      BtnLogin.innerHTML = "logging ... ";
      login(InputUser,InputPassword);
      BtnLogin.innerHTML = "login Success ";
    }
    else{
      alert('please fill username & password')
    }
  }
  handleSignUp(){
    let InputUser = elementById('username').value.trim();
    let InputPassword = elementById('password').value.trim();
    if(validatInput(InputUser,InputPassword) === 'true'){
      if(InputPassword.length >= 8){
        let BtnSignUp = elementById('signup');
        BtnSignUp.innerHTML = "SignUp ...";
        signUp(InputUser,InputPassword);
        BtnSignUp.innerHTML = " SignUp and Success";
      } else{ alert('Minimum password length is 8 characters')}
  }
  else{
      alert('please fill username & password')
    }
  }
  render(){
//         <img src={config.icons.tinder} style={{width: 60}} />

    return (
      <div>
        <TinderLogo>
           <img src={config.icons.tinder}  />
        </TinderLogo>
        <P>Welcome</P>
        <Input id="username" placeholder="User Name" type="text" />
        <Input id="password" placeholder="password" type="password" />
        <ButtonContainer >
          <Button id='login' style={{ marginRight:"20px"}} onClick={this.handleLogin}>Login</Button>
          <Button id="signup" onClick={this.handleSignUp}>SignUp</Button>
        </ButtonContainer>
        </div>
    );
  }
}
//sign up with username & password here
function signUp (username,password){
   var url = config.url.signup;
  var requestOptions = {
        "method": "POST",
        "headers": {
            "Content-Type": "application/json",
        }
    };
    var body = {
        "provider": "username",
        "data": {
            "username": username,
            "password": password,
        }
    };

    requestOptions.body = JSON.stringify(body);
    fetch(url, requestOptions)
    .then(function(response) {
    	return response.json();
    })
    .then(function(result) {
      if(result.detail === null){
        let BtnSignUp = elementById('signup');
        BtnSignUp.innerHTML = "Sign-in";
        alert('user already have try another username');
      }
      else{
    	 // To save the auth token received to offline storage
    	 var authToken = result.auth_token
    	 window.localStorage.setItem('HASURA_AUTH_TOKEN', authToken);
       window.localStorage.setItem('C_ID', result.hasura_id);
       takeToAccountCreate(result);
     }
       // Navigate to the Location.reload article
      //document.location.assign('https://developer.mozilla.org/en-US/docs/Web/API/Location.reload');
    })
    .catch(function(error) {
      let BtnSignUp = elementById('signup');
      BtnSignUp.innerHTML = "Sign-in";
    	console.log('Request Failed:' + error);
    });
}
