import "./App.css";
import { routes } from "./routes";
import Header from "./components/Header";
import Footer from "./components/Footer";
import ScrollTop from "./containers/ScrollTop";
import CustomizedSnackbars from "./containers/Snackbar";
import {
  BrowserRouter as Router,
  Route,
  Redirect,
  Switch,
} from "react-router-dom";

function App() {
  return (
    <Router>
      <div>
        <CustomizedSnackbars />
        <Header />
        <Switch>
          {routes.map((route, idx) => {
            return (
              route.component && (
                <Route
                  key={idx}
                  path={route.path}
                  exact={route.exact}
                  render={(props) => <route.component {...props} />}
                />
              )
            );
          })}
          <Redirect from="/" to="/home" />
        </Switch>
        <Footer />
        <ScrollTop />
      </div>
    </Router>
  );
}

export default App;
