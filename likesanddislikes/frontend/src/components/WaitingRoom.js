import {
	Box,
	Button,
	Heading,
	propNames,
	Text,
	VStack,
} from "@chakra-ui/react";
import React, { useState } from "react";
import { useParams } from "react-router-dom";
import "../App.css";

export default function WaitingRoom(props) {
	const [playersInLobby, setPlayersInLobby] = useState([
		"dom",
		"nivy",
		"kyle",
	]);
	const { roomId } = useParams();

	const startGame = async function (event) {
		event.preventDefault();
		const path = "/" + roomId + "/selectChoices";
		props.history.push({
			pathname: path,
			state: {
				player_id: player_id,
			},
		});
	};

	let player_id = props.location.state.player_id;

	return (
		<div class="centered">
			<VStack>
				<Heading>Waiting for players... {player_id}</Heading>
				<Text textAlign="center">Room code: {roomId}</Text>
				<Text textAlign="center">{`${playersInLobby.length} players in the room`}</Text>
				<Box boxShadow="xl" backgroundColor="red" pl={40} pr={40}>
					{playersInLobby.map((player) => (
						<Text>{player}</Text>
					))}
				</Box>
				<Button onClick={startGame}>Start Game</Button>
				<Button>Back</Button>
			</VStack>
		</div>
	);
}
