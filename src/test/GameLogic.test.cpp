#include <catch2/catch_test_macros.hpp>

#include "../main/GameLogic.cpp"

TEST_CASE( "should init", "[test]" ) {
    GameLogic game;
    CellPlayerData* cell000 = game.getCellPlayerData({ Side::FRONT, 0, 0}, 0);
    CellPlayerData* cell100 = game.getCellPlayerData({ Side::FRONT, 1, 0}, 0);
    Player* player0 = game.getPlayer(0);

    REQUIRE( cell000->atPosition == true );
    REQUIRE( cell000->activeTrail == true );
    REQUIRE( cell000->ownedBy == false );
    REQUIRE( cell100->atPosition == false );
    REQUIRE( cell100->activeTrail == false );
    REQUIRE( cell100->ownedBy == false );
    REQUIRE( player0->direction == Direction::RIGHT );
}

TEST_CASE( "should move player", "[test]" ) {
    GameLogic game;
    CellPlayerData* cell000 = game.getCellPlayerData({ Side::FRONT, 0, 0}, 0);
    CellPlayerData* cell100 = game.getCellPlayerData({ Side::FRONT, 1, 0}, 0);
    Player* player0 = game.getPlayer(0);

    game.tick();

    REQUIRE( cell000->atPosition == false );
    REQUIRE( cell000->activeTrail == true );
    REQUIRE( cell000->ownedBy == false );
    REQUIRE( cell100->atPosition == true );
    REQUIRE( cell100->activeTrail == true );
    REQUIRE( cell100->ownedBy == false );
    REQUIRE( player0->direction == Direction::RIGHT );
}



TEST_CASE( "should own simple square", "[test]" ) {
    GameLogic game;
    CellPlayerData* cell000 = game.getCellPlayerData({ Side::FRONT, 0, 0}, 0);
    CellPlayerData* cell100 = game.getCellPlayerData({ Side::FRONT, 1, 0}, 0);
    CellPlayerData* cell110 = game.getCellPlayerData({ Side::FRONT, 1, 1}, 0);
    CellPlayerData* cell010 = game.getCellPlayerData({ Side::FRONT, 0, 1}, 0);
    Player* player0 = game.getPlayer(0);

    player0->direction = Direction::RIGHT;
    game.tick();
    player0->direction = Direction::UP;
    game.tick();

    REQUIRE( cell000->atPosition == false );
    REQUIRE( cell000->activeTrail == true );
    REQUIRE( cell000->ownedBy == false );

    REQUIRE( cell100->atPosition == false );
    REQUIRE( cell100->activeTrail == true );
    REQUIRE( cell100->ownedBy == false );

    REQUIRE( cell110->atPosition == true );
    REQUIRE( cell110->activeTrail == true );
    REQUIRE( cell110->ownedBy == false );

    REQUIRE( cell010->atPosition == false );
    REQUIRE( cell010->activeTrail == false );
    REQUIRE( cell010->ownedBy == false );


    player0->direction = Direction::LEFT;
    game.tick();

    REQUIRE( cell000->atPosition == false );
    //REQUIRE( cell000->activeTrail == false );
    //REQUIRE( cell000->ownedBy == true );

    REQUIRE( cell100->atPosition == false );
    //REQUIRE( cell100->activeTrail == false );
    //REQUIRE( cell100->ownedBy == true );

    REQUIRE( cell110->atPosition == false );
    //REQUIRE( cell110->activeTrail == false );
    //REQUIRE( cell110->ownedBy == true );

    REQUIRE( cell010->atPosition == true );
    //REQUIRE( cell010->activeTrail == false );
    //REQUIRE( cell010->ownedBy == true );
}