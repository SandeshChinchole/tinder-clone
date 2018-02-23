import React from 'react';
import ReactDOM from 'react-dom';
import styled from 'styled-components';
import './global-styles';
import {Login, takeToHome} from "./module"
import {Drover} from './home'
import {config} from './config'

const Banner = styled.div`
  height: 500px;
  background-color: #fff;
  max-width: 400px;
  min-width: 300px;
  margin: 0 auto;
  margin-top: 10px;
  margin-top: 100px;
  border: 1px solid #dfe9f2;
  border-radius: 13px;
  box-shadow: 0px 0px 20px 4px #ad181830;
`;
const Container = styled.div`
  width: 100%;
  height: 100%;
  display: flex;
  font-size: 24px;
  justify-content: center;
  align-items: center;
  color: #02020266
`;
const Load = (
   <Container>Loading....</Container>
);

   // process start here
    ReactDOM.render(
      Load,
      document.getElementById('root')
    );
    setTimeout(7000)
    checkLogin();



function checkLogin(){
    var url = config.url.user_info;

    // If you have the auth token saved in offline storage
    var authToken = window.localStorage.getItem('HASURA_AUTH_TOKEN');
    // headers = { "Authorization" : "Bearer " + authToken }
    var requestOptions = {
        "method": "GET",
        "headers": {
            "Content-Type": "application/json",
            "Authorization":  "Bearer " + authToken
        }
    };

    fetch(url, requestOptions)
    .then(function(response) {
    	return response.json();
    })
    .then(function(result) {
      if(result.message !== 'invalid authorization token'){
        ReactDOM.render(
          <Container>Authenticating...</Container>,
          document.getElementById('root')
        );
        window.localStorage.setItem('C_ID', result.hasura_id);
        takeToHome(result);
      }
      else{
        takeToLogin();
      }
    })
    .catch(function(error) {
    	console.log('Request Failed:' + error);
      alert('something went wrong check your network ...')
    });
}
export function takeToLogin(){
  ReactDOM.render(
    <Banner >
      <Login />
    </Banner> ,
    document.getElementById('root')
  );
}
