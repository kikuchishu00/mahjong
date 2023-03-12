// import React from 'react';
// import ReactDOM from 'react-dom';
// import Sleep from './components/App';
// // import Root from './components/App';
// ReactDOM.render(<Sleep />, document.getElementById('sleep'));
import React, { StrictMode } from "react";
import { createRoot } from "react-dom/client";

import App from "./components/App";

const root = createRoot(document.getElementById("root"));
root.render(
//   <StrictMode>
    <App />
//   </StrictMode>
);
