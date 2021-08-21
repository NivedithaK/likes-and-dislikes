import MyForm from './components/MyForm';
import WaitingRoom from './components/WaitingRoom';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";

function App() {
  return (
    <Router>
      <Switch>
        <Route exact path="/" component={MyForm} / >
        <Route path="/:room_id/waiting" component={WaitingRoom} />
      </Switch>
    </Router>
  );
}

export default App;
