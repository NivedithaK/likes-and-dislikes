import MyForm from './components/MyForm';
import WaitingRoom from './components/WaitingRoom';
import SelectChoices from './components/SelectChoices';
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
        <Route exact path="/" component={MyForm} />
        <Route path="/:roomId/waiting" component={WaitingRoom} />
        <Route path="/:roomId/selectChoices" component={SelectChoices} />
      </Switch>
    </Router>
  );
}

export default App;
