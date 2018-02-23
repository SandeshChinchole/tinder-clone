import {config} from './config';
import {takeToLogin} from "./index";

export function logout(){
  var url = config.url.logout;

  // If you have the auth token saved in offline storage
   var authToken = window.localStorage.getItem('HASURA_AUTH_TOKEN');
  // headers = { "Authorization" : "Bearer " + authToken }
  var requestOptions = {
      "method": "POST",
      "headers": {
          "Content-Type": "application/json",
          "Authorization": "Bearer " + authToken
      }
  };

  fetch(url, requestOptions)
  .then(function(response) {
  	return response.json();
  })
  .then(function(result) {
    takeToLogin();
  })
  .catch(function(error) {
  	console.log('Request Failed:' + error);
  });
}

// detete the account
export function deleteAccount(){
   // origin are resiticted yet.
   alert('all user info are deleted');
    var url = config.url.delete_user;
    // If you have the auth token saved in offline storage
     var authToken = window.localStorage.getItem('HASURA_AUTH_TOKEN');
    // headers = { "Authorization" : "Bearer " + authToken }
    // get user by auth token put it on hasura_id
    var requestOptions = {
        "method": "POST",
        "headers": {
            "Content-Type": "application/json",
            "Authorization": "Bearer "+authToken,
        }
    };
    var body =   {};
    requestOptions.body = JSON.stringify(body);

    fetch(url, requestOptions)
    .then(function(response) {
    	return response.json();
    })
    .then(function(result) {
      if(result.message !== "delete-user request failed"){
        takeToLogin()
      }else{
        alert("please try again")
        return false;
      }
    })
    .catch(function(error) {
    	console.log('Request Failed:' + error);
    });
}
