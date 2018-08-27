//
// Created by Han Xiao on 2018-09-22.
//

#include <iostream>
#include <string>
#include <ofstream>
/*
 * Transforms text files into csv file to be read in Python or R
 * */

int main(int argc, char[] * argv){
    std::ifstream fs;
    fs.open(argv[1]);
    std::string word;
    std::cin >> word;
    fs << word;
    while(std::cin >> word){
        fs << "," + word;
    }
}