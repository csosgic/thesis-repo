#include <utility>

// maybe change those values
// i dont know the real life acceptable values
// will make it to allow for +-50% of the default values
pair<int, int> data_rate_peer_to_peer_acceptable_range(20000000, 60000000);
pair<int, int> delay_peer_to_peer_acceptable_range(1, 5);
pair<int, int> data_rate_cluster_acceptable_range(5000000, 15000000);
pair<int, int> delay_cluster_acceptable_range(1, 5);

// those values will be used to fix them if they are outside the safe range
int data_rate_peer_to_peer_optimal_value = 40000000;
int delay_peer_to_peer_optimal_value = 3;
int data_rate_cluster_optimal_value = 10000000;
int delay_cluster_optimal_value = 3;


bool network_intrusion_detection (
    int data_rate_peer_to_peer,
    int delay_peer_to_peer,
    int data_rate_cluster,
    int delay_cluster
){    
    cout << "starting network analysis" << endl;
    int changes_detected = 0;
    // here we can either stop the simulation but in real life thats not a solution

    // if any of the following if statements are true then we can either stop the sim of fix the values
    // i dont know what the real life equivilant of fixing the values manually

    // the other option is to change the values to acceptable values

    // if it is just IDS we can suspend the programm until an admin decides what to do 
    // if it is an IPS we can have it change the values
    if (
        data_rate_peer_to_peer < data_rate_peer_to_peer_acceptable_range.first || data_rate_peer_to_peer > data_rate_peer_to_peer_acceptable_range.second
    ){
        cout << "\t data_rate_peer_to_peer is outside of normal range of values" << endl;
        changes_detected++;
        data_rate_peer_to_peer = data_rate_peer_to_peer_optimal_value;
    }

    if(
        delay_peer_to_peer < delay_peer_to_peer_acceptable_range.first || delay_peer_to_peer > delay_peer_to_peer_acceptable_range.second
    ){
        cout << "\t delay_peer_to_peer is outside of normal range of values" << endl;
        changes_detected++;
        delay_peer_to_peer = delay_peer_to_peer_optimal_value;
    }

    if(
        data_rate_cluster < data_rate_cluster_acceptable_range.first || data_rate_cluster > data_rate_cluster_acceptable_range.second
    ){
        cout << "\t data_rate_cluster is outside of normal range of values" << endl;
        changes_detected++;
        data_rate_cluster = data_rate_cluster_optimal_value;
    }

    if(
        delay_cluster < delay_cluster_acceptable_range.first || delay_cluster > delay_cluster_acceptable_range.second
    ){
        cout << "\t delay_cluster is outside of normal range of values" << endl;
        changes_detected++;
        delay_cluster = delay_cluster_optimal_value;
    }

    if(changes_detected != 0){
        cout << "ids detected " << changes_detected << " threats" << endl;
        return 0;
    }else{
        cout << "ids didnt detect any threats" << endl;
        return 1;
    }
}
