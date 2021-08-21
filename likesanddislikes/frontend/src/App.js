import MyForm from './components/MyForm';
import WaitingRoom from './components/WaitingRoom';
import SelectChoices from './components/SelectChoices';
import {
  Switch,
  Route,
  useHistory
} from "react-router-dom";
import React from "react";

function App() {
  const history = useHistory();
  return (
			<Switch>
				<Route exact path="/" component={MyForm} />
				<Route
					path="/:roomId/waiting"
					component={WaitingRoom}
					history={history}
				/>
				<Route
					path="/:roomId/selectChoices"
					component={SelectChoices}
					history={history}
				/>
			</Switch>
  );
}

export default App;