APP_TSX_CONTENT = """
import React from "react";
import { Route, Routes, BrowserRouter, Navigate } from "react-router-dom";
import Home from "./src/pages/home";
import { APP_URLS } from "./src/helpers";

function App() {
  return (
      <BrowserRouter>
        <Routes>
          <Route path={APP_URLS.home} element={<Home />} />
          <Route path="*" element={<Navigate to={APP_URLS.home} />} />
        </Routes>
      </BrowserRouter>
  );
}
export default App;
"""

INDEX_TSX_CONTENT = """

import React from "react";
import ReactDOM from "react-dom/client";
import { Provider } from "react-redux";
import { ToastContainer } from "react-toastify";
import "bootstrap/dist/css/bootstrap.min.css"; // don't change order
import "react-toastify/dist/ReactToastify.css";
import App from "./App";
import { LoadingIndicator, FeedbackToast } from "./src/components";
import reduxStore from "./src/redux/store";

const rootElement = document.getElementById("root");

if (rootElement) {
  const root = ReactDOM.createRoot(rootElement);
  root.render(
    <React.StrictMode>
      <Provider store={reduxStore}>
        <LoadingIndicator />
        <App />
        <ToastContainer newestOnTop={true} />
        <FeedbackToast />
      </Provider>
    </React.StrictMode>,
  );
}
"""
HOME_PAGE_CONTENT = """
import React, { useEffect } from "react";
import { Container, Button } from "react-bootstrap";
import { showCustomFeedbackToast, showLoadingIndicator } from "../redux/actions";
import { useAppDispatch } from "../hooks";
const Home = () => {
  const dispatch = useAppDispatch();

  useEffect(() => {
    dispatch(
      showCustomFeedbackToast(
        "Welcome to my hybrid Django-React project",
        "info",
      ),
    );
  }, []);
  const load = () => {
    dispatch(showLoadingIndicator(true));
    setTimeout(() => {
        dispatch(showLoadingIndicator(false));
    }, 3000);

  };
  return (
    
    <Container className="d-flex flex-column justify-content-center align-items-center vh-100 text-center">
      <h1 className="mb-4">My Bootstrapped Hybrid Django-React Project</h1>
      <Button variant="primary" size="lg" onClick={load}>
        Test Loader
      </Button>
    </Container>
  );
};

export default Home;
"""
