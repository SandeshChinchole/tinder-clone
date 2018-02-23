import React from 'react';
import ReactDOM from 'react-dom';
import styled from 'styled-components'
import {suggestU, Suggest} from "./suggestion"
import {config} from './config'
// loading icons
const NopeIcon = config.icons.nopeIcon;
const LikeIcon = config.icons.likeIcon;
const tinderUrl   = config.icons.tinder;
const Back = config.icons.backIcon;
const CenterPannel = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
`;
const Pannel_1 = styled.div`
  background: #fff;
  border: 1px solid #0003;
  border-radius: 18px;
  height: 600px;
  width: 375px;
  margin-top: 90px;
  display: grid;
  grid-template-rows: 0.1fr 1fr;
  grid-template-columns: 1fr;
  overflow: scroll;
`;
const IconCon = styled.div`
  height: 35px;
  width: 35px;
  padding: 7px;
  color: red;
`;
const Head = styled.div`
grid-row-start: 1;
grid-row-end: 2;
    box-shadow: 0 0 4px #0000002e;
`;
const Middle = styled.div`
 padding: 0 1px;
 overflow: hidden;
`;
const Bottom = styled.div`
`;
const Matches = styled.div`
 width: 100%;
 height: 100%;
 background: #fff;
 display: grid;
 grid-template-columns: 1fr;
 grid-template-rows: repeat(3, 69px);
 grid-gap: 0px;
 margin-top: 10px;
 grid-auto-rows: 69px;
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
 grid-template-columns: 2.2fr 4fr;
`;
 const Ava = styled.img`
  width: 50px;
  height: 50px;
  border-radius: 100%;
 `;

// makeing list item custom
class Item extends React.Component {
   constructor(props) {
      super(props);
    }
     render(){
       let picUrl  = config.url.file+"/"+this.props.pic;
       return (
         <Row >
           <div style={{display:"flex",justifyContent:"center",alignItems:"center"}}>
               <Ava src={picUrl}></Ava>
           </div>
           <div style={{ fontSize: 18 ,display: "flex", justifyContent:"start",alignItems: "center",borderBottom: "1px solid rgba(206, 193, 193, 0.53)"}}><p>{this.props.name}</p></div>
         </Row>
     )
   }
 }

export class Match extends React.Component{
  constructor(props){
    super(props);
    this.handleClick = this.handleClick.bind(this);
  }
// handle the setting putton
 handleClick(){
// nothing work here but update the current suggestion
ReactDOM.render(<Suggest current={this.props.current} all={this.props.all} H_id={this.props.H_id} name={this.props.name} id={this.props.id} />,document.getElementById('desktop'))
 }
render(){
   match();
    return(
      <CenterPannel>
        <Pannel_1>
          <Head>
            <div style={{display:"grid", gridTemplateColumns:"0.7fr 1fr"}}>
               <div style={{display:"flex",justifyContent:"start",marginRight: -10}}>
                 <img onClick={this.handleClick} style={{borderRadius: "100%", border:" 2px solid #fff",width: "72px",height:" 26px", marginTop: 21}} src={Back} />
               </div>
               <div  style={{display:"flex",justifyContent:"start",marginRight: 30}}>
                <img  style={{borderRadius: "100%", border:" 2px solid #fff",width: "66px",height:" 47px", marginTop: 14}} src={tinderUrl} />
              </div>
           </div>
          </Head>
          <Middle>
            <Matches id="match">
            </Matches>
          </Middle>
        </Pannel_1>
      </CenterPannel>
    );
  }
}
export function match(){

              var url = config.url.like_users;
              let listItems;
                  // If you have the auth token saved in offline storage
                  var authToken = window.localStorage.getItem('HASURA_AUTH_TOKEN');
                  // headers = { "Authorization" : "Bearer " + authToken }
              var requestOptions = {
                "method": "GET",
                "headers": {
                  "Content-Type": "application/json",
                  "Authorization": "Bearer "+authToken
                  }
                };
                fetch(url, requestOptions)
                .then(function(response) {
                return response.json();
                })
                .then(function(result) {
                    listItems = result['result'].slice(1,result['result'].length).map(a => <Item id={a[0]} name={a[1]} pic={a[2]} />);
                     ReactDOM.render(listItems,document.getElementById('match'))
                })
                .catch(function(error) {
                console.log('Request Failed:' + error);
                });

}
