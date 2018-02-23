import { injectGlobal } from 'styled-components';
/* eslint no-unused-expressions: 0 */
injectGlobal`
 *{
   margin: 0;
   padding: 0;
 }
  body{
    color: #14171a;
    font-size: 14px;
    line-height: 20px;
    font-family: ProximaNova,sans-serif;
    line-height: 1.3125;
  }
  ::placeholder { /* Chrome, Firefox, Opera, Safari 10.1+ */
    color:  #b3b3b3;
    opacity: 1; /* Firefox */
  }

`;
