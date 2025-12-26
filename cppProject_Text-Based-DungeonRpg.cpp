#include <iostream>
using std::cout;
using std::cin;
using std::endl;
using std::string;

/*
	DEVELOPER REMINDER
	PLAYER STATS: DMG, HP, STM
	DMG = (PTS * 0.5) + 10
	HP = (PTS * 0.5) + 10
	STM = (PTS * 0.5) + 20;
*/

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class Player{
public:
	int dmg(int pts) {
		int damage = (pts * 0.5) + 5;
		return damage;
	}
	
	int hp(int pts) {
		int health = (pts * 0.5) + 10;
		return health;
	}
	
	int stm(int pts) {
		int stamina = (pts * 0.5) + 20;
		return stamina;
	}
}; 
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class GUI{
public:
	void stat_sheet(string name, int hp, int dmg, int stamina, int pts){
		cout << "=================================================================== " << endl;
		cout << "                       STAT SHEET FOR DUMMIES                       " << endl;
		cout << "=================================================================== " << endl;
		cout << " CHARACTER NAME: " << name << endl;
		cout << " - - - > HEALTH: " << hp << endl;
		cout << " - - - > DAMAGE: " << dmg << endl;
		cout << " - - - > STAMINA: " << stamina << endl;
		cout << " Unspent Points: " << pts << endl;
		cout << "=================================================================== " << endl;
	}
};
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void env(){
	// Define Variables
	Player Player;
	GUI GUI;
	string char_name;
	string user_select;
	// End
	
	// Player Values
	int player_hp, player_stamina, player_damage;
	int hp_point, dmg_point, stm_point, stored_point;
	
	stored_point = 30;
	hp_point = 0;
	dmg_point = 0;
	stm_point = 0;
		
	player_hp = Player.hp(hp_point);
	player_damage = Player.dmg(dmg_point);
	player_stamina = Player.stm(stm_point);
	//End
	
	// Main Env
	cout << "=================================================================== " << endl;
	cout << "            TEXT-BASED DUNGEON DELVER ROLE PLAYING GAME             " << endl;	
	cout << "=================================================================== " << endl;
	cout << "- - - > Input Character Name: ";
	cin >> char_name;
	cout << endl;
	cout << "------------------------------------------------------------------- " << endl;
	for (int i = 0;/*NULL*/;i++){
		cout << "=================================================================== " << endl;
		cout << "            TEXT-BASED DUNGEON DELVER ROLE PLAYING GAME             " << endl;	
		cout << "=================================================================== " << endl;
		cout << " Character Name: " << char_name << endl;
		cout << " Select Action: " << endl;
		cout << " ---> Check Stat Sheet <1>" << endl;
		cout << " ---> Level Up         <2>" << endl;
		cout << " ---> Enter Dungeon    <3>" << endl;
		cout << " ---> Exit Game        <4>" << endl;
		cout << " Choice: ";
		cin >> user_select;
		cout << "------------------------------------------------------------------- " << endl;
		if (user_select == "1") { // CHECK STAT SHEET 
		
			GUI.stat_sheet(char_name, player_hp, player_damage, player_stamina, stored_point);
			
		}else if (user_select == "2") { // LEVEL UP 
		
			
			
		}else if (user_select == "3") { // ENTER DUNGEON
			cout << "" << endl;
		}else if (user_select == "4") { // EXIT GAME
			cout << "EXITING GAME. . . " << endl;
			break;
		}else {
			cout << " Invalid Choice. . ." << endl;
			cout << " Try Again. . . ." << endl;
			
		}
	}
}
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
int main(void){
	string user_in;
	for (int i = 0;/*Null*/;i++){
		// - - - - - - - - - - - - - - - - - - - - - - - - > Main
		env();	
		// < - - - End
		// - - - - - - - - - - - - - - - - - - - - - - - - > START 
		cout << "Terminate Session? <Y/N>: ";
		if (user_in == "Y" || user_in == "y"){
			cout << "Terminating Session. . . " << endl;
			break;
		}else if (user_in == "N" || user_in == "n") {
			cout << "Resuming Session. . ." << endl;
			continue;
		}else { 
			cout << "Invalid Input. . . " << endl;
			continue;
		}
		// - - - - - - - - - - - - - - - - - - - - - - - - > END
	}
	return 0;
}
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
