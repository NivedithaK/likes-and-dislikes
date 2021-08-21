import {
	FormControl,
	FormLabel,
	FormErrorMessage,
	FormHelperText,
	Input,
	Button,
	Stack,
	Text,
	Box,
} from "@chakra-ui/react";
import React, { useState } from "react";
import axios from "axios";
import { useHistory } from "react-router-dom";
import bgimg from "../assets/background.png";

const url = "";

export default function MyForm(props) {
	const history = useHistory();
	const [roomCode, setRoomCode] = useState("");
	const [name, setName] = useState("");
	const [roomError, setRoomError] = useState("");
	const [nameError, setNameError] = useState("");

	const handleSubmit = async function (event) {
		event.preventDefault();
		let hasError = false;
		if (roomCode.trim() === "") {
			setRoomError(
				"You must set the room code if you are trying to join a game"
			);
			hasError = true;
		} else {
			setRoomError("");
		}

		if (name.trim() === "") {
			setNameError("Name cannot be empty");
			hasError = true;
		} else {
			setNameError("");
		}

		if (hasError) {
			return;
		}

		const headers = {
			"Content-Type": "application/json",
		};
		axios
			.post(
				`http://127.0.0.1:8000/likes-and-dislikes/join-lobby/`,
				{ nickname: name, lobby_id: roomCode },
				{ headers }
			)
			.then((result) => {
				if (result.status === 201) {
					let data = result.data;
					const path = "/" + roomCode + "/waiting";
					console.log(path);
					history.push(path, {
						players_in_lobby: data.players_in_lobby,
						lobby_id: roomCode,
					});
				}
			});
	};

	const createNewRoom = async function (event) {
		event.preventDefault();
		if (name.trim() === "") {
			setNameError("Name cannot be empty");
			return;
		} else {
			setNameError("");
		}
		const headers = {
			"Content-Type": "application/json",
		};

		axios
			.post(
				`http://127.0.0.1:8000/likes-and-dislikes/create-lobby-and-host/`,
				{ nickname: name },
				{ headers }
			)
			.then((result) => {
				if (result.status === 201) {
					let data = result.data;
					let lobbyId = data.lobby_code;
					let player_id = data.player_id;
					const path = "/" + lobbyId + "/waiting";
					console.log(path);
					history.push({
						pathname: path,
						state: {
							player_id: player_id,
							players_in_lobby: data.players_in_lobby,
							lobby_id: lobbyId,
						},
					});
				}
			});
	};

	return (
		<Box
			height="100vh"
			width="100vw"
			backgroundSize="100vw 100vh"
			bgImage={bgimg}
			class="centered"
		>
			<Stack
				backgroundColor="white"
				p={20}
				maxWidth={500}
				margin="auto"
				spacing={5}
				borderRadius="30"
			>
				<Text fontSize="4xl">Likes and Dislikes</Text>

				<form onSubmit={handleSubmit}>
					<FormControl isInvalid={roomError}>
						<FormLabel htmlFor="room-code">Room code</FormLabel>
						<Input
							type="text"
							id="roomCode"
							onChange={({ target }) =>
								setRoomCode(target.value.trim())
							}
						/>
						<FormErrorMessage>{roomError}</FormErrorMessage>
					</FormControl>
					<FormControl isInvalid={nameError}>
						<FormLabel htmlFor="name">Name</FormLabel>
						<Input
							type="text"
							id="name"
							onChange={({ target }) => setName(target.value)}
						/>
						<FormErrorMessage>{nameError}</FormErrorMessage>

						<Stack spacing={3} marginTop={10} align="center">
							<Button type="submit">Enter</Button>
							<Button onClick={createNewRoom}>
								Make a new room
							</Button>
						</Stack>
					</FormControl>
				</form>
			</Stack>
		</Box>
	);
}
