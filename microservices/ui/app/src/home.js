import React from 'react';
import styled from 'styled-components';
import ReactDOM from 'react-dom';
import {Edit} from "./edit-profile"
import {suggestU, Suggest} from "./suggestion"
import {config} from "./config";
import {takeToLogin} from "./index"
import {logout,deleteAccount} from "./api-call"

const Icon_1 = config.icons.edit;
const Icon   = config.icons.setting;
const tinderUrl   = config.icons.tinder;


const Navbar = styled.div`
  width: 100%;
  box-shadow: 0 1px 8px 0 rgba(0,17,25,.27);
  height: 70px;
  background: linear-gradient(262deg,#ff7854,#fd267d);
`;

const Pannel = styled.div`
  width: 25%;
  height: 100%;
  position: reative;
  background: #fff;
  box-shadow: -1px 2px 9px #0000007a;
`;
const Desktop = styled.div`
  background-color: #f5f7fa;
  width: 100%;
  height: 100%;
  border-left: 1px solid #d0d0d0cf;
  position: relative;
`;
const Tar = styled.div`
   color: #fff;
   display: flex;
   font-size: 17px;
   padding: 10px 0px 0px 20px;
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

  const IconCon = styled.div`
  height: 28px;
  width: 28px;
  padding: 5px 10px 8px 5px;
  border-radius: 100%;
  border: 1px solid #0000004d;
`;

const Button = styled.button`
    background: #ff6868;
    padding: 10px 20px;
    width: 81%;
    margin-top: 10px;
    margin: 0 auto;
      margin-top: 0px;
    margin-top: 14px;
    color: #fff;
    font-weight: bold;
`;
 const P = styled.div`
   margin-top: 24px;
   margin-left: 10px;
 `;
 const Input = styled.input`
     padding: 5px 20px;
     margin-left: 8px;
     margin-top: 4px;
 `;
 const Matches = styled.div`
  width: 100%;
  background: #fff;
  display: grid;
  grid-template-columns: 1fr;
  grid-template-rows: repeat(3, 60px);
  grid-gap: 0px;
  margin-top: 10px;
  grid-auto-rows: 60px;
  justify-items: center;
  justify-content: center;
  align-items: stretch;
  overflow: scroll;
 `;

 const Row = styled.div`
  width: 100%;
  height: 100%;
  background: #fff;
  display: grid;
  grid-template-columns: 1.6fr 4fr;
 `;

  const Ava = styled.img`
   width: 45px;
   height: 44px;
   border-radius: 100%;
  `;

// makeing list item custom
class Item extends React.Component {
    constructor(props) {
       super(props);
      this.handleItmes = this.handleItmes.bind(this);
     }
     handleItmes(){
       ReactDOM.render(<Suggest current={this.props.c} all={this.props.a} H_id={this.props.id} name={this.props.name} id={this.props.pic} />,document.getElementById('desktop'))
     }
      render(){
        let picUrl  = config.url.file+"/"+this.props.pic;
        return (
          <Row onClick={this.handleItmes}>
            <div style={{display:"flex",justifyContent:"center",alignItems:"center"}}>
                <Ava src={picUrl}></Ava>
            </div>
            <div style={{ fontSize: 18 ,display: "flex", justifyContent:"start",alignItems: "center",borderBottom: "1px solid rgba(206, 193, 193, 0.53)"}}><p>{this.props.name}</p></div>
          </Row>
      )
    }
  }

class LogoutPage extends React.Component{
  constructor(props) {
   super(props);
   this.handleDone = this.handleDone.bind(this);
   this.handleDeleteAC = this.handleDeleteAC.bind(this);
 }
 // handle some event here
  handleDone(){
   const btnInput = document.getElementById('City').value;
   const InputLook = document.getElementById('look').value;
    if(btnInput !== "" & InputLook!==""){
      // make some AJAX call to set location
         ReactDOM.render(<EditProfile current={this.props.current} sugest={this.props.sugest} userInfo={this.props.userInfo}/>,document.getElementById('desktop'))
    }
    else{
      if(btnInput !== "")
      alert('please input  a valid City name');
      if(InputLook!=="")
      alert('please input  what you are looking for');
      else{
        alert("please input something here.")
      }
    }
  }
  handleLogout(){
   logout();
   //origin are resiticted yet try in real app
   takeToLogin()
  }
  handleDeleteAC(){
    //origin are resiticted yet try in real app
    let BtnDelete = document.getElementById('delete');
    BtnDelete.innerHTML = "deleting..."
    deleteAccount(this.props.userInfo);
  }
  render(){
    return (
      <CenterPannel>
        <Pannel_1>
          <div style={{display:"flex",justifyContent:"center"}}>
            <div>
              <P>City</P>
              <Input id='City' placeholder="Enter City Name" type="text" ></Input>
              <P> Looking for</P>
              <Input id='look' placeholder="male/female" type="text" ></Input>
            </div>
          </div>
            <div style={{marginTop: 100,display:'grid'}}>
              <Button onClick={this.handleDone}>Done</Button>
              <Button onClick={this.handleLogout}>Logout</Button>
              <Button id="delete" onClick={this.handleDeleteAC}>Delete Account</Button>
          </div>
        </Pannel_1>
      </CenterPannel>
    );
  }
}

export class EditProfile extends React.Component{
  constructor(props) {
   super(props);
   this.handleSetting = this.handleSetting.bind(this);
   this.handletoS = this.handletoS.bind(this);
   this.handleEdit = this.handleEdit.bind(this);
 }
  // handle the setting putton
  handleEdit(){
    //hadle onClick
    ReactDOM.render(<Edit current={this.props.current} sugest={this.props.sugest} userInfo={this.props.userInfo} email={this.props.userInfo.email} H_id={this.props.userInfo.hasura_id} name={this.props.userInfo.name} id={this.props.userInfo.profile_file_id} />,document.getElementById('desktop'))
  }
   handleSetting(){
     ReactDOM.render(<LogoutPage current={this.props.current} sugest={this.props.sugest} userInfo={this.props.userInfo} />,document.getElementById('desktop'))
   }
  handletoS(){
   let i = this.props.current;
    ReactDOM.render(<Suggest current={this.props.current} all={this.props.sugest} H_id={this.props.sugest[i].hasura_id} name={this.props.sugest[i].name} id={this.props.sugest[i].profile_file_id} />,document.getElementById('desktop'))
  }

  render(){
    let userDetails = this.props.userInfo;
    let url = config.url.file+"/"+userDetails.profile_file_id;
    let username = userDetails.name;
    let gender= userDetails.gender;
    let email = userDetails.email;
   let age = userDetails.age;
    return(
      <CenterPannel>
        <Pannel_1 id="edit">
          <div style={{display:"grid", gridTemplateColumns:"1fr 1fr"}}>
            <div style={{display:"flex",justifyContent:"flex-end",marginRight: -10}}>
              <img style={{borderRadius: "100%", border:" 2px solid #fff",width: "50px",height:" 40px", marginTop: 12}} src={url} />
            </div>
            <div style={{display:"flex",justifyContent:"flex-end",marginRight: 30}}>
              <img onClick={this.handletoS} style={{borderRadius: "100%", border:" 2px solid #fff",width: "50px",height:" 40px", marginTop: 12}} src={tinderUrl} />
            </div>
          </div>
          <img style={{border:"1px solid #0000004d", height: "56%",width:260, margin:"20 45 10 45", borderRadius:"7px"}} src={url} />
          <p style={{textAlign: "center" ,fontSize:20}}> {username+", "+age} </p>
          <div style={{display: 'flex'}}>
            <IconCon style={{marginLeft: 15, fontSize:'14px' }} >
              <img style={{borderRadius: "100%", border:" 2px solid #fff",height:" 28px"}} onClick={this.handleSetting} src={Icon} />
                <p style={{fontSize:"1.2em", margin:"5px 0px 0px -10px", color: "#00000080"}}>Settings</p>
            </IconCon>
            <IconCon style={{marginLeft: 220 }}>
              <img onClick={this.handleEdit} style={{borderRadius: "100%", border:" 2px solid #fff",height:" 28px"}} src={Icon_1} />
                <p style={{fontSize:"1.2em", margin:"5px 0px 0px -10px", color:" #00000080"}}>EditInfo</p>
            </IconCon>
          </div>
        </Pannel_1>
      </CenterPannel>
    );
  }
}

export class Drover extends React.Component{
  constructor(props) {
   super(props);
   this.handleEditProfile = this.handleEditProfile.bind(this);
 }
  handleEditProfile(){
   ReactDOM.render(<EditProfile current={0} userInfo={this.props.logedUser} sugest={this.props.userInfo}/>,document.getElementById('desktop'))
   }

  render(){
      let userDetails = this.props.logedUser;;
      const currentUser_id =this.props.id;
      const allUser = this.props.userInfo;
      const length = this.props.userInfo.length;

      const listItems = allUser.map((allUsers,i) => allUsers.hasura_id!==currentUser_id && <Item c={i} a={allUser} id={allUsers.hasura_id} name={allUsers.name} pic={allUsers.profile_file_id} />);

      let url = config.url.file+"/"+userDetails.profile_file_id;
      let username = userDetails.name;
      let gender= userDetails.gender;
      let email = userDetails.email;
       //   load All User And put it it on match like here
    return (
      <div style={{display:"flex",height:"100%"}}>
        <Pannel>
          <Navbar>
            <Tar onClick={this.handleEditProfile}>
              <img style={{borderRadius: "100%", border:" 2px solid #fff",width:"45px",height:" 40px"}} src={url} />
              <p style={{marginTop: 7, marginLeft: 10}}>{username}</p>
            </Tar>
          </Navbar>
          <Matches id="allu">
            {listItems}
          </Matches>
        </Pannel>
        <Desktop id="desktop">
          <Suggest current={0} all={this.props.userInfo}  H_id={allUser[0].hasura_id} name={allUser[0].name} id={allUser[0].profile_file_id} />
        </Desktop>
      </div>
    );
  }
}
