import React from 'react';
import styled from 'styled-components';
import {EditProfile} from './home'
import ReactDOM from 'react-dom'
import {config} from './config'
const Body = styled.div`
  display: grid;
  grid-template-rows: 143px  1.5fr;
  grid-template-columns: 1fr;
`;
 const P = styled.div`
   margin-top: 7px;
   margin-left: 10px;
 `;
 const Input = styled.input`
     padding: 3px 20px;
     margin-left: 8px;
     margin-top: 2px;
 `;
 const Textarea = styled.textarea`
     padding: 5px 20px;
     margin-left: 8px;
     margin-top: 2px;
     width: 287px;
     height: 39px;
 `;
 const Button = styled.button`
     background: #ff6868;
     padding: 10px 20px;
     width: 81%;
     margin: 0 auto;
     color: #fff;
     font-weight: bold;
 `;
 const CenterPannel = styled.div`
   display: flex;
   justify-content: center;
   align-items: center;
 `;
 const Pannel_1 = styled.div`
   background: #fff;
   border: 1px solid #0003;
   border-radius: 18px;
   height: 450px;
   width: 353px;
   margin-top: 90px;
   display: block;
 `;
// this component hadle editing of profile yes.
export class Edit extends React.Component {
  constructor(props){
    super(props);
    this.handleDone = this.handleDone.bind(this);
    this.handleUpdate = this.handleUpdate.bind(this);
    this.state = {  userName :this.props.name,userEmail:this.props.email,age:this.props.userInfo.age,about:this.props.userInfo.about_me  };
    this.onChangeName = this.onChangeName.bind(this);
    this.onChangeEmail = this.onChangeEmail.bind(this);
    this.onChangeAge = this.onChangeAge.bind(this);
    this.onChangeAbout = this.onChangeAbout.bind(this);
  }
  onChangeName(event) {
    this.setState({
      userName: event.target.value
    });
  }
  onChangeAge(event) {
    this.setState({
      age: event.target.value
    });
  }
  onChangeAbout(event) {
    this.setState({
      about: event.target.value
    });
  }
  onChangeEmail(event) {
    this.setState({
      userEmail: event.target.value
    });
  }
  handleDone(){
    ReactDOM.render(<EditProfile current={this.props.current} sugest={this.props.sugest} userInfo={this.props.userInfo}/>,document.getElementById('desktop'))
  }
  handleUpdate(){
        const name = document.getElementById("name").value;
        const age = document.getElementById("age").value;
        const about = document.getElementById("about").value;
        const email = document.getElementById('email').value;
        const Btn = document.getElementById("update");
        Btn.innerHTML ="Updating.."
          let user = this.props.userInfo;
          user.name = name;
          user.email = email;
          user.age = age;
          user.about_me = about;
        var url = config.url.update_user;
        const hid = this.props.H_id;
      // If you have the auth token saved in offline storage
       var authToken = window.localStorage.getItem('HASURA_AUTH_TOKEN');
      // headers = { "Authorization" : "Bearer " + authToken }
      var requestOptions = {
          "method": "POST",
          "headers": {
              "Content-Type": "application/json",
              "Authorization": "Bearer "+authToken
          }
      };

      var body = {
                  "email": email,
                  "name": name,
                  "age": age,
                  "about_me": about
              };

      requestOptions.body = JSON.stringify(body);

      fetch(url, requestOptions)
      .then(function(response) {
      	return response.json();
      })
      .then(function(result) {
        })
      .catch(function(error) {
      	console.log('Request Failed:' + error);
      });
      ReactDOM.render(<EditProfile current={this.props.current} sugest={this.props.sugest} userInfo={user}/>,document.getElementById('desktop'))

  }

  render(){
     let url = config.url.file+"/"+this.props.id;
     const hid = this.props.H_id;
     const name = this.props.name;
    return (
      <CenterPannel>
        <Pannel_1>
        <Body>
          <div style={{display:"flex",justifyContent:"center"}}>
            <img style={{width: "81%",marginTop: "10px"}} src={url} />
          </div>
          <div style={{display:"flex",justifyContent:"center"}}>
            <div>
              <P>Name</P>
              <Input id='name' placeholder="username" type="text"
              value={this.state.userName}
              onChange={this.onChangeName}    ></Input>
              <P>Age</P>
              <Input id='age' placeholder="age" type="text"
              value={this.state.age}
              onChange={this.onChangeAge}></Input>
              <P>Email</P>
              <Input id='email' placeholder="Email" type="text"
              value={this.state.userEmail}
              onChange={this.onChangeEmail} ></Input>
              <P>About me</P>
              <Textarea id="about" rows="4" cols="50" placeholder="about me" wrap="hard"
                value={this.state.about}
                onChange={this.onChangeAbout}  />
              <div style={{marginTop: 10,display:'grid',gridTemplateColumns:"1fr 1fr"}}>
                <Button style={{background:"#fff",color:"#ff6868"}} onClick={this.handleDone}>Cancel</Button>
                <Button id="update" onClick={this.handleUpdate}>Update</Button>
            </div>
            </div>
          </div>
        </Body>
        </Pannel_1>
      </CenterPannel>
    );
  }
}
