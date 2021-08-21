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
import bgimg from "../assets/background.png";

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

	const backPage = async function (event) {
		event.preventDefault();
		const path = "/";
		props.history.push({
			pathname: path,
		});
	};

	let player_id = props.location.state.player_id;

	return (
		<Box backgroundSize="100vw 100vh" bgImage={bgimg}>
			<div class="centered">
				<VStack
					backgroundColor="white"
					p={20}
					maxWidth={520}
					margin="auto"
					spacing={5}
					borderRadius="30"
				>
					<Heading>Waiting for players...</Heading>
					<Text textAlign="center">Room code: {roomId}</Text>
					<Text
						pb={5}
						textAlign="center"
					>{`${playersInLobby.length} players in the room`}</Text>
					<Box
						boxShadow="lg"
						border="2px"
						borderColor="gray.200"
						pl={40}
						pr={40}
						pt={3}
						pb={3}
						borderRadius={6}
					>
						{playersInLobby.map((player) => (
							<Text>{player}</Text>
						))}
					</Box>
					<Button onClick={startGame}>Start Game</Button>
					<Button onClick={backPage}>Back</Button>
				</VStack>
			</div>
		</Box>
	);
}
//UVHSWJ
