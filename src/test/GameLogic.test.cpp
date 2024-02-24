#include <catch2/catch_test_macros.hpp>

#include "../main/GameLogic.cpp"


#include <cstdint>

uint32_t factorial( uint32_t number ) {
    return number <= 1 ? number : factorial(number-1) * number;
}

TEST_CASE( "Should init", "[factorial]" ) {
    GameLogic game;
    CellPlayerData* cell000 = game.getCellPlayerData(0, 0, 0);
    CellPlayerData* cell100 = game.getCellPlayerData(1, 0, 0);

    REQUIRE( cell000->atPosition == true );
    REQUIRE( cell000->activeTrail == true );
    REQUIRE( cell000->ownedBy == false );
    REQUIRE( cell100->atPosition == false );
    REQUIRE( cell100->activeTrail == false );
    REQUIRE( cell100->ownedBy == false );
}