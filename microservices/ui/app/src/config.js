import EditIcon from "./../assets/edit.svg";
import LeftAngleIcons from "./../assets/left-angle-bracket.svg"
import LikeIcon from "./../assets/like.svg"
import NopeIcon from "./../assets/nope.svg"
import SettingIcon from "./../assets/setting.svg"
import LogoIcon from "./../assets/logo.jpg"
import LogoCropIcon from "./../assets/logocrop.png"
import LikeUserIcon from "./../assets/like_user.svg"

//now no need to  react refrence becoz here we use jsx element and need a React reference at compile time to make an element using  React.creatElement
//you may hardcoded the clustername but alternative and best is i think.
//if your hostname is ui.cluster-name.hasura-app.io then cluste name can be get using this.
const clusterName = window.location.hostname.split('.')[1];
const host  = clusterName+".hasura-app.io";
export let config = {
    url:{
        //url for api-end point
          file:"https://filestore."+host+"/v1/file",
          data:"https://data."+host+"/v1/query",
          logout:"https://auth."+host+"/v1/user/logout",
          user_info:"https://auth."+host+"/v1/user/info",
          login: "https://auth."+host+"/v1/login",
          signup:"https://auth."+host+"/v1/signup",
          delete_user:"https://api."+host+"/delete",
          insert_user:"https://api."+host+"/insert-user",
          update_user:"https://api."+host+"/update-user",
          like_users:"https://api."+host+"/like-users",
          like:"https://api."+host+"/like",
          nope:"https://api."+host+"/nope",
          getUsersInfo: "https://api."+host+"/get-allusers-info",
        },
  icons:{
            edit:EditIcon,
            setting:SettingIcon,
            likeUserIcon:LikeUserIcon,
            nopeIcon:NopeIcon,
            likeIcon:LikeIcon,
            backIcon:LeftAngleIcons,
            tinder:LogoIcon,
            tinderNameLogo: LogoCropIcon,
        }
  };
