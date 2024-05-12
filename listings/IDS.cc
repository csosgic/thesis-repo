#include <iostream>
#include <utility>

using namespace std;

// maybe change those values
// i dont know the real safe values
// will make it to allow for +-50% of the default values
pair<int, int> data_rate_peer_to_peer_safe_range(20000000, 60000000);
pair<int, int> delay_peer_to_peer_safe_range(1, 5);
pair<int, int> data_rate_cluster_safe_range(5000000, 15000000);
pair<int, int> delay_cluster_safe_range(1, 5);
bool network_intrusion_detection (
    int data_rate_peer_to_peer,
    int delay_peer_to_peer,
    int data_rate_cluster,
    int delay_cluster
){    
    int changes_detected = 0;
    // here we can either stop the simulation but in real life thats not a solution

    // if any of the following if statements are true then we can either stop the sim of fix the values
    // i dont know what the real life equivilant of fixing the values manually

    // the other option is to change the values to acceptable values

    // if it is just IDS we can suspend the programm until an admin decides what to do 
    // if it is an IPS we can have it change the values
    if (
        data_rate_peer_to_peer < data_rate_peer_to_peer_safe_range.first || data_rate_peer_to_peer > data_rate_peer_to_peer_safe_range.second
    ){
        cout << "\t data_rate_peer_to_peer is outside of normal range of values" << endl;
        changes_detected++;
        data_rate_peer_to_peer = 40000000;
    }

    if(
        delay_peer_to_peer < delay_peer_to_peer_safe_range.first || delay_peer_to_peer > delay_peer_to_peer_safe_range.second
    ){
        cout << "\t delay_peer_to_peer is outside of normal range of values" << endl;
        changes_detected++;
        delay_peer_to_peer = 3;
    }

    if(
        data_rate_cluster < data_rate_cluster_safe_range.first || data_rate_cluster > data_rate_cluster_safe_range.second
    ){
        cout << "\t data_rate_cluster is outside of normal range of values" << endl;
        changes_detected++;
        data_rate_cluster = 10000000;
    }

    if(
        delay_cluster < delay_cluster_safe_range.first || delay_cluster > delay_cluster_safe_range.second
    ){
        cout << "\t delay_cluster is outside of normal range of values" << endl;
        changes_detected++;
        delay_cluster = 3;
    }

    if(changes_detected != 0){
        cout << "ids detected " << changes_detected << " threats" << endl;
        return 0;
    }else{
        cout << "ids didnt detect any threats" << endl;
        return 1;
    }
}


int main(){
    cout << "starting network analysis" << endl;

    //network_intrusion_detection(int data_rate_peer_to_peer, int delay_peer_to_peer, int data_rate_cluster, int delay_cluster)
    
    
    cout << "##############################################" << endl;
    cout << "attack 1:" << endl;
    network_intrusion_detection(40000000, 3, 1000000, 100);
    cout << "##############################################" << endl << endl << endl;

    cout << "##############################################" << endl;
    cout << "attack 2:" << endl;
    network_intrusion_detection(1000000, 3, 100, 3);
    cout << "##############################################" << endl << endl << endl;

    cout << "##############################################" << endl;
    cout << "attack 3:" << endl;
    network_intrusion_detection(40000000, 3, 5000000, 50);
    cout << "##############################################" << endl << endl << endl;

    cout << "##############################################" << endl;
    cout << "attack 4:" << endl;
    network_intrusion_detection(1000000, 10, 10000000, 3);
    cout << "##############################################" << endl << endl << endl;

    cout << "##############################################" << endl;
    cout << "attack 8:" << endl;
    network_intrusion_detection(40000000, 3, 2000000, 50);
    cout << "##############################################" << endl << endl << endl;

    cout << "##############################################" << endl;
    cout << "attack 9:" << endl;
    network_intrusion_detection(3000000, 70, 10000000, 3);
    cout << "##############################################" << endl << endl << endl;


    return 0;
}